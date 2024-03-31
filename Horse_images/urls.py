from django.urls import path
from .views import Add_picture, Delete_image
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("image_add",Add_picture.as_view()),
    path("image_delete",Delete_image.as_view()),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)