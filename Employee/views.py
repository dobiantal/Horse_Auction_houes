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
        token = jwt.encode(token_layers, 'secret', algorithm='RS256').decode('utf-8')

        response = Response()
        response.set_cookie(key='token',value=token, httponly=True)
        response.data = {'token':token}

        return response

