from django.urls import path
from .views import Insert_Country, Update_Country, Delete_Country, Get_one_Country, Get_all_Countries
urlpatterns = [
    path('country_add', Insert_Country.as_view()),
    path('country_update/<str:id>', Update_Country.as_view()),
    path('country_delete/<str:id>', Delete_Country.as_view()),
    path('country_get_one/<str:id>', Get_one_Country.as_view()),
    path('country_getall', Get_all_Countries.as_view()),
]