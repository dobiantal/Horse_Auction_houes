from django.urls import path
from Employee.views import EmpRegistrate, EmpLogIn, EmpIsLogedIn, EmpLogOut

urlpatterns = [
    path('emp_registrate', EmpRegistrate.as_view()),
    path('emp_login', EmpLogIn.as_view()),
    #path('user',EmpIsLogedIn.as_view()),#Nem biztos hogy kell ha vissza tudok térni backenden belül.
    path('emp_logout',EmpLogOut.as_view())

]
