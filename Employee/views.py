import json

from rest_framework.response import Response
from rest_framework.views import APIView
from Employee.serializer import EmployeeSerializer, EmpInnerJoinSerializer
from Employee.models import Employee
from rest_framework import status
import jwt, datetime
from django.contrib.auth.hashers import check_password
from Authenticate.Check_emp import Emp_auth_checker
from Response_messages.Messages import Response_message
class EmpRegistrate(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            token = request.COOKIES.get('emptoken')
            token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
            if token_layers['policy'] == "Executive Director":
                Empserializer = EmployeeSerializer(data=request.data)
                if Empserializer.is_valid():
                    Empserializer.save()
                    return Response(self.Success("Employee","added"))
            else:
                return Response({"message":"Access denied! This action use only ED"})
        else:
            self.UnAuthenticated()

class EmpLogIn(APIView,Response_message):
    def post(self,request):
        account_name = request.data['account_name']
        password = request.data['password']

        emp = Employee.objects.filter(account_name=account_name).first()
        serializerd = EmpInnerJoinSerializer(emp)
        policy = serializerd.data.get('policy_id').get('policy')
        if emp is None:
            self.NotFound("Employee")
        if not check_password(password,emp.password):
            self.IncorretPW()

        extra_token_data = {'policy': str(policy)}
        # I have to insert the policy into the token.
        token_layers = {
            'id': emp.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            **extra_token_data
        }
        token = jwt.encode(token_layers, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='emptoken',value=token, httponly=True)
        response.data = {'emptoken':token},status.HTTP_200_OK
        return response

class EmpLogOut(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('emptoken')
        response.data = {"message":"Logged out!"},status.HTTP_200_OK
        return response