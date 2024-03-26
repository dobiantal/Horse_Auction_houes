from django.urls import path
from Employee.views import EmpRegistrate,EmpLogIn,EmpLogOut
urlpatterns = [
    path('emp_reg',EmpRegistrate.as_view()),
    path('emp_login',EmpLogIn.as_view()),
    path('emp_logout',EmpLogOut.as_view()),
]
