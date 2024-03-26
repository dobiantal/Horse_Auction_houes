from rest_framework.response import Response
from rest_framework.views import APIView
from Employee.serializer import EmployeeSerializer
from Employee.models import Employee
from rest_framework import status
import jwt, datetime
from django.contrib.auth.hashers import check_password
from Authenticate.Check_emp import Check_emp_auth
from Response_messages.Messages import BadModel, UnAuthenticated, Success, NotFound, IncorretPW
class EmpRegistrate(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            token = request.COOKIES.get('emptoken')
            token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
            is_boss = Employee.objects.filter(id=token_layers['id']).first()
            serializerd = EmployeeSerializer(is_boss, many=True)
            if serializerd.policy == "Executive Director":
                Empserializer = EmployeeSerializer(data=request.data)
                Empserializer.is_valid(raise_exception=True)
                Empserializer.save()
                Success("Employee","added")
            else:
                return Response({"message":"Access denied! This action use only ED"})
        else:
            UnAuthenticated()

class EmpLogIn(APIView):
    def post(self,request):
        account_name = request.data['account_name']
        password = request.data['password']

        emp = Employee.objects.filter(account_name=account_name).first()
        if emp is None:
            NotFound("Employee")
        if not check_password(password,emp.password):
            IncorretPW()

        # I have to insert the policy into the token.
        token_layers = {
            'id': emp.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
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