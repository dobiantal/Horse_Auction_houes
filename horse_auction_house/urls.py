from django.urls import path, include

urlpatterns = [
    path('api/', include('Employee.urls')),
    path('api/',include('Bidder.urls')),
    path('api/',include('Beeders.urls')),
    path('api/',include('Cities.urls')),
    path('api/',include('Countries.urls'))
]
"""path('api/',include('Horse_images.urls')),
    path('api/',include('Horses.urls')),
    path('api/',include('Policy.urls')),
    path('api/',include('Sale_state.urls')),
    path('api/',include('Sport_specifications.urls')),"""
