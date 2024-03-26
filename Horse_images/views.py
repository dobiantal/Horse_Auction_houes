from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Horse_images
from .serializer import Horse_imagesSerializer
from Authenticate.Check_emp import Check_emp_auth
from Response_messages.Messages import Success, BadModel, UnAuthenticated
class Add_picture(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            serializered = Horse_imagesSerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                Success("Horse image","added")
            else:
                BadModel("picture inserting")
        else:
            UnAuthenticated()
class Delete_image(APIView):
    def delete(self,request,id):
        if Check_emp_auth(request) == True:
            image = Horse_images.objects().filter(id=id).first()
            image.delete()
            Success("Horse images", "delete picture")
        else:
            UnAuthenticated()