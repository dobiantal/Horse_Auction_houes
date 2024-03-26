from rest_framework.response import Response
from rest_framework.views import APIView
import jwt, datetime
from Bidder.serializer import BidderSerializer
from Bidder.models import Bidder
from Authenticate.Check_emp import Check_emp_auth
from Authenticate.Check_bidder import Check_bidder_auth
from Response_messages.Messages import Success, UnAuthenticated, BadModel, NotFound, IncorretPW
from rest_framework import status

class BidderRegistrate(APIView):
    def post(self,request):
        Bidderserializer = BidderSerializer(data=request.data)
        if Bidderserializer.is_valid():
            Bidderserializer.save()
            Success("Bidder","registration")
        else:
            BadModel("Registration")
class Bidder_Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        bidder = Bidder.objects.filter(Username=username).first()
        if bidder is None:
            NotFound("Bidder")
        if not bidder.check_password(password):
            IncorretPW()
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
class Get_all_Bidder(APIView):
    def get(self,request):
        if Check_emp_auth(request) == True:
            all = Bidder.objects.all()
            serialized = BidderSerializer(all, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()
class Get_one_Bidder(APIView):
    def get(self,request,id):
        if Check_emp_auth(request) == True:
           bideer = Bidder.objects.filter(id=id).first()
           serialized = BidderSerializer(bideer)
           return serialized.data,status.HTTP_200_OK
        else:
            UnAuthenticated()
class Update_Bidder(APIView):
    def post(self,request, id):
        if Check_bidder_auth(request) == True:
            bidder = Bidder.objects.filter(id=id).first()
            serialzered = BidderSerializer(data=bidder,instance=request.data)
            if serialzered.is_valid():
                serialzered.save()
                Success("Bidder","update")
            else:
                BadModel("Updating")
        else:
            UnAuthenticated()
class Delete_Bidder(APIView):
    def delete(self,request, id):
        if Check_bidder_auth(request) == True:
            bidder = Bidder.objects.filter(id=id).first()
            bidder.delete()
            Success("Bidder","delete")
        else:
            UnAuthenticated()