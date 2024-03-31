from django.urls import path
from .views import Update_sport_spec, Get_Sport_spec, Insert_sport_spec, Delete_Sport_spec

urlpatterns =[
    path("sport-spec_add",Insert_sport_spec.as_view()),
    path("sport-spec_update/<str:id>",Update_sport_spec.as_view()),
    path("sport-spec_get",Get_Sport_spec.as_view()),
    path("sport-spec_delete/<str:id>",Delete_Sport_spec.as_view())
]