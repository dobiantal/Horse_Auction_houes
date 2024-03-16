from django.urls import path
from Employee.views import Registrate

urlpatterns = [
    path('registrate', Registrate.as_view()),
]
