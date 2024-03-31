from rest_framework.response import Response
from rest_framework.views import APIView
import jwt, datetime
from Bidder.serializer import BidderSerializer
from Bidder.models import Bidder
from Authenticate.Check_emp import Emp_auth_checker
from Authenticate.Check_bidder import Bidder_auth_checker
from Response_messages.Messages import Response_message
from rest_framework import status

class BidderRegistrate(APIView,Response_message):
    def post(self,request):
        Bidderserializer = BidderSerializer(data=request.data)
        if Bidderserializer.is_valid():
            Bidderserializer.save()
            self.Success("Bidder","registration")
        else:
            self.BadModel("Registration")
class Bidder_Login(APIView,Response_message):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        bidder = Bidder.objects.filter(Username=username).first()
        if bidder is None:
            self.NotFound("Bidder")
        if not bidder.check_password(password):
            self.IncorretPW()
        token_layers = {
            'id': bidder.id,
            'u_name':bidder.Username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(token_layers, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='bid_token', value=token, httponly=True)
        response.data = {'bid_token': token},status.HTTP_200_OK

        return response

class Bidder_LogOut(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('bid_token')
        response.data = {"message":"You have been logged out"},status.HTTP_200_OK
        return response
class Get_all_Bidder(APIView,Emp_auth_checker,Response_message):
    def get(self,request):
        if self.Check_emp_auth(request) == True:
            all = Bidder.objects.all()
            serialized = BidderSerializer(all, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()
class Get_one_Bidder(APIView,Emp_auth_checker,Response_message):
    def get(self,request,id):
        if self.Check_emp_auth(request) == True:
           bideer = Bidder.objects.filter(id=id).first()
           serialized = BidderSerializer(bideer)
           return serialized.data,status.HTTP_200_OK
        else:
            self.UnAuthenticated()
class Update_Bidder(APIView,Bidder_auth_checker,Response_message):
    def post(self,request, id):
        if self.Check_bidder_auth(request) == True:
            bidder = Bidder.objects.filter(id=id).first()
            serialzered = BidderSerializer(data=bidder,instance=request.data)
            if serialzered.is_valid():
                serialzered.save()
                self.Success("Bidder","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_Bidder(APIView,Bidder_auth_checker,Response_message):
    def delete(self,request, id):
        if self.Check_bidder_auth(request) == True:
            bidder = Bidder.objects.filter(id=id).first()
            bidder.delete()
            self.Success("Bidder","delete")
        else:
            self.UnAuthenticated()