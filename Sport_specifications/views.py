from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sport_specification
from .serializer import Sport_specSerializer
from Authenticate.Check_emp import Emp_auth_checker
from Response_messages.Messages import Response_message

class Get_Sport_spec(APIView,Emp_auth_checker):
    def get(self,request):
        if self.Check_emp_auth(request) == True:
            sport_spec = Sport_specification.objects.all()
            serializered = Sport_specSerializer(sport_spec, many=True)
            return Response(serializered.data,status.HTTP_200_OK)
class Insert_sport_spec(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            serializered = Sport_specSerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                self.Success("Sale state","insert")
            else:
                self.BadModel("Inserting")
        else:
            self.UnAuthenticated()
class Update_sport_spec(APIView,Emp_auth_checker,Response_message):
    def post(self,request, id):
        if self.Check_emp_auth(request) == True:
            sport_spec = Sport_specification.objects().filter(id=id).first()
            serializerd = Sport_specSerializer(data=sport_spec, instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                self.Success("Sport specification","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_Sport_spec(APIView,Emp_auth_checker,Response_message):
    def delete(self,request, id):
        if self.Check_emp_auth(request)== True:
            sport_spec = Sport_specification.objects().filter(id=id).first()
            sport_spec.delete()
            self.Success("Sport specification", "delete")
        else:
            self.UnAuthenticated()

