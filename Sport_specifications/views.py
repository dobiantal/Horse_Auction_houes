from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sport_specification
from .serializer import Sport_specSerializer
from Authenticate.Check_emp import Check_emp_auth
from Response_messages.Messages import Success, UnAuthenticated, BadModel

class Get_Sport_spec(APIView):
    def get(self,request):
        if Check_emp_auth(request) == True:
            sport_spec = Sport_specification.objects.all()
            serializered = Sport_specSerializer(sport_spec, many=True)
            return Response(serializered.data,status.HTTP_200_OK)
class Insert_sport_spec(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            serializered = Sport_specSerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                Success("Sale state","insert")
            else:
                BadModel("Inserting")
        else:
            UnAuthenticated()
class Update_sport_spec(APIView):
    def post(self,request, id):
        if Check_emp_auth(request) == True:
            sport_spec = Sport_specification.objects().filter(id=id).first()
            serializerd = Sport_specSerializer(data=sport_spec, instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                Success("Sport specification","update")
            else:
                BadModel("Updating")
        else:
            UnAuthenticated()
class Delete_Sport_spec(APIView):
    def delete(self,request, id):
        if Check_emp_auth(request)== True:
            sport_spec = Sport_specification.objects().filter(id=id).first()
            sport_spec.delete()
            Success("Sport specification", "delete")
        else:
            UnAuthenticated()

