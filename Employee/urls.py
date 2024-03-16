from django.urls import path
from Employee.views import Registrate, LogIn, IsLogedIn,LogOut

urlpatterns = [
    path('registrate', Registrate.as_view()),
    path('login', LogIn.as_view()),
    path('user',IsLogedIn.as_view()),#Nem biztos hogy kell ha vissza tudok térni backenden belül.
    path('logout',LogOut.as_view())

]
