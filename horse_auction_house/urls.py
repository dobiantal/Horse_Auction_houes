from django.urls import path, include

urlpatterns = [
    path('api/', include('Employee.urls')),
    path('api/',include('Bidder.urls')),
    path('api/',include('Beeders.urls')),
    path('api/',include('Cities.urls')),
    path('api/',include('Countries.urls'))
]
