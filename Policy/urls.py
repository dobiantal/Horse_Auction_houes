from django.urls import path
from .views import AddPolicy, UpdatePolicy, DeletePolicy

urlpatterns = [
    path("add_policy",AddPolicy.as_view()),
    path("update_policy/<str:id>",UpdatePolicy.as_view()),
    path("delete_policy/<str:id>",DeletePolicy.as_view()),

]