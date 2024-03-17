from django.urls import path, include

urlpatterns = [
    path('api/', include('Employee.urls')),
    path('api/',include('Bidder.urls'))
]
