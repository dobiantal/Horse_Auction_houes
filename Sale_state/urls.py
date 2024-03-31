from django.urls import path
from .views import Insert_sale_state, Get_Sale_State, Upldate_sale_state, Delete_sale_state

urlpatterns = [
    path("sale_state_add",Insert_sale_state.as_view()),
    path("sale_state_get-all",Get_Sale_State.as_view()),
    path("sale_state_update-state/<str:id>",Upldate_sale_state.as_view()),
    path("sale_state_delete-state/<str:id>",Delete_sale_state.as_view())
]