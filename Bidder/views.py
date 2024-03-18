from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from Bidder.serializer import BidderSerializer
from Bidder.models import Bidder
from Employee.views import EmpIsLogedIn
from Exceptions.projectExceptions import FailedUpdatingException,FailedDeleteexception,FailedInsertException
class BidderRegistrate(APIView):
    def post(self,request):
        Bidderserializer = BidderSerializer(data=request.data)
        if Bidderserializer.is_valid():
            Bidderserializer.save()
            return Response({
                "message":"Registration successful"
            })
        else:
            raise FailedInsertException()
class Bidder_Login(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        bidder = Bidder.objects.filter(Username=username).first()
        if bidder is None:
            raise AuthenticationFailed('Bidder is not registered')
        if not bidder.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        token_layers = {
            'id': bidder.id,
            'u_name':bidder.Username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(token_layers, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {'token': token}

        return response
class Bidder_isLoggedIn(APIView):
    def get(self,request):
        token = request.COOKIE.get('token')
        if not token:
            return False
        try:
            token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False

        bidder = Bidder.objects.filter(id=token_layers['id']).first()
        serialized = BidderSerializer(bidder)
        return serialized.data
class Bidder_LogOut(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('token')
        response.data = {"message":"You have been logged out"}
        return response
class Get_all_Bidder(APIView):
    def get(self,request):
        if EmpIsLogedIn() == True:
            all = Bidder.objects.all()
            serialized = BidderSerializer(all)
            return serialized.data
        else:
            raise AuthenticationFailed('Unauthenticated! Please login!')
class Get_one_Bidder(APIView):
    def get(self,request,id):
        if EmpIsLogedIn() == True:
           bideer = Bidder.objects.filter(id=id).first()
           serialized = BidderSerializer(bideer)
           return serialized.data
        else:
            raise AuthenticationFailed('Unauthenticated! Please login!')
class Update_Bidder(APIView):
    def post(self,request, id):
        if Bidder_isLoggedIn() == True:
            bidder = Bidder.objects.filter(id=id).first()
            serialzered = BidderSerializer(data=bidder,instance=request.data)
            if serialzered.is_valid():
                serialzered.save()
                return Response({"message":"Update has been successful!"})
            else:
                raise FailedUpdatingException()
class Delete_Bidder(APIView):
    def delete(self,request, id):
        if Bidder_isLoggedIn() == True:
            bidder = Bidder.objects.filter(id=id).first()
            bidder.delete()
            return Response({"message":"Delete has been successful!!"})
        else:
            raise AuthenticationFailed("Unauthenticated!!Please login!!")