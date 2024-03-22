from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Horse_images
from .serializer import Horse_imagesSerializer
from Employee.views import EmpIsLogedIn

class Add_picture(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            serializered = Horse_imagesSerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                return Response({'message':'Picture save has been saved!'})
            else:
                return Response({'message:':'Error! The picture uploading failed!'})
        else:
            return Response({'message':'Unauthenticated! Please login!'})
class Delete_image(APIView):
    def delete(self,request,id):
        if EmpIsLogedIn() == True:
            image = Horse_images.objects().filter(id=id).first()
            image.delete()
            return Response({'message':'The image has been deleted!'})
        else:
            return Response({'message':'Unauthenticated! Please login!'})