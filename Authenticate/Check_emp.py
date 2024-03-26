import jwt
from Employee.models import Employee
def Check_emp_auth(request):
    token = request.COOKIES.get('emptoken')
    if not token:
        return False
    try:
        token_layers = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return False

    emp = Employee.objects.filter(id=token_layers['id']).first()
    if emp is not None:
        return True