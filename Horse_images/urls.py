from django.urls import path
from .views import Add_picture, Delete_image
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)