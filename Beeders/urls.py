from django.urls import path
from Beeders.views import Insert_Beeder, Get_All_Breeder, Get_One_Breeder,Update_Breeder,Delete_Breeder
urlpatterns = [
    path('breeder_reg',Insert_Beeder.as_view()),
    path('breeder_all',Get_All_Breeder.as_view()),
    path('breeder_one/<str:id>',Get_One_Breeder.as_view()),
    path('breeder_update/<str:id>',Update_Breeder.as_view()),
    path('breeder_delete/<str:id>',Delete_Breeder.as_view()),
]