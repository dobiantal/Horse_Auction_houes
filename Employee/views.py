from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from Employee.serializer import EmployeeSerializer
from Employee.models import Employee
import jwt, datetime
class Registrate(APIView):
    def post(self,request):
        Empserializer = EmployeeSerializer(data=request.data)
        Empserializer.is_valid(raise_exception=True)
        Empserializer.save()
        return Response({
            "message":"Registration successful"
        })
class LogIn(APIView):
    def post(self,request):
        account_name = request.data['account_name']
        password = request.data['password']

        print(password)
        emp = Employee.objects.filter(account_name=account_name).first()
        if emp is None:
            raise AuthenticationFailed('User not found!')
        if not emp.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        token_layers = {
            'id': emp.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(token_layers, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='token',value=token, httponly=True)
        response.data = {'token':token}

        return response

class IsLogedIn(APIView):
    def get(self,request):
        token = request.COOKIES.get('token')
        if not token:
            raise AuthenticationFailed("UnAuthenticated!")
        try:
            token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("UnAuthenticated!")

        emp = Employee.objects.filter(id=token_layers['id']).first()
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data)
        #Meg kell nézni hogy ha csak simán serializer.data térünk vissza akkor igényli-e hogy Responsal kell visszatérni.

class LogOut(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('token')
        response.data = {"message":"Logged out!"}
        return response