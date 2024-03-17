from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from Employee.serializer import EmployeeSerializer
from Employee.models import Employee
import jwt, datetime
class EmpRegistrate(APIView):
    def post(self,request):
        Empserializer = EmployeeSerializer(data=request.data)
        Empserializer.is_valid(raise_exception=True)
        Empserializer.save()
        return Response({
            "message":"Registration successful"
        })
class EmpLogIn(APIView):
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
        token = jwt.encode(token_layers, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='emptoken',value=token, httponly=True)
        response.data = {'emptoken':token}

        return response

class EmpIsLogedIn(APIView):
    def get(self,request):
        token = request.COOKIES.get('emptoken')
        if not token:
            return False
        try:
            token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise False

        emp = Employee.objects.filter(id=token_layers['id']).first()
        serializer = EmployeeSerializer(emp)
        return serializer.data

class EmpLogOut(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('emptoken')
        response.data = {"message":"Logged out!"}
        return response