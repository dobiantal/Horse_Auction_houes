import jwt
from Employee.models import Employee
class Emp_auth_checker:
    def Check_emp_auth(self,request):
        self.token = request.COOKIES.get('emptoken')
        if not self.token:
            return False
        try:
            token_layers = jwt.decode(self.token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False

        self.emp = Employee.objects.filter(id=token_layers['id']).first()
        if self.emp is not None:
            return True