from django.urls import path
from Cities.views import Insert_city, Get_All_City, Get_One_City, Update_City, Delete_city
urlpatterns = [
    path('insert_city', Insert_city.as_view()),
    path('getall_city', Get_All_City.as_view()),
    path('getone_city/<str:id>', Get_One_City.as_view()),
    path('update_city/<str:id>', Update_City.as_view()),
    path('delete_city/<str:id>', Delete_city.as_view()),
]