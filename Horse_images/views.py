from rest_framework.views import APIView
from .models import Horse_images
from .serializer import Horse_imagesSerializer
from Authenticate.Check_emp import Emp_auth_checker
from Response_messages.Messages import Response_message
class Add_picture(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            serializered = Horse_imagesSerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                self.Success("Horse image","added")
            else:
                self.BadModel("picture inserting")
        else:
            self.UnAuthenticated()
class Delete_image(APIView,Emp_auth_checker,Response_message):
    def delete(self,request,id):
        if self.Check_emp_auth(request) == True:
            image = Horse_images.objects().filter(id=id).first()
            image.delete()
            self.Success("Horse images", "delete picture")
        else:
            self.UnAuthenticated()