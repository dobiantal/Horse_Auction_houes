from django.urls import path
from .views import Add_Horse,Update_Horse, Delete_Horse, Update_price, Get_all_horse,Get_only_OnBid

urlpatterns = [
    path("horse_add",Add_Horse.as_view()),
    path("horse_update/<str:id>",Update_Horse.as_view()),
    path("horse_delete/<str:id>",Delete_Horse.as_view()),
    path("horse_update-price",Update_price.as_view()),
    path("horse_all-horse",Get_all_horse.as_view()),
    path("horse_on-bidding",Get_only_OnBid.as_view()),
]