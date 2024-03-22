from django.urls import path
from .views import Insert_Country, Update_Country, Delete_Country, Get_one_Country, Get_all_Countries
urlpatterns = [
    path('', Insert_Country.as_view()),
    path('', Update_Country.as_view()),
    path('', Delete_Country.as_view()),
    path('', Get_one_Country.as_view()),
    path('', Get_all_Countries.as_view()),
]