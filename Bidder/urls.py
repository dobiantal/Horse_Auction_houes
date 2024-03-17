from django.urls import path
from Bidder.views import BidderRegistrate, Bidder_Login, Bidder_LogOut, Get_all_Bidder, Get_one_Bidder
urlpatterns = [
    path('bidder_reg',BidderRegistrate.as_view()),
    path('bidder_login',Bidder_Login.as_view()),
    path('bidder_logout',Bidder_LogOut.as_view()),
    path('bidder_getAll',Get_all_Bidder.as_view()),
    path('bidder_getOne',Get_one_Bidder.as_view()),
]