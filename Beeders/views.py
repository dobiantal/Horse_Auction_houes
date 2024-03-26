from rest_framework.response import Response
from rest_framework.views import APIView
from Beeders.serializer import BeederSerializer
from Beeders.models import Beeders
from Authenticate.Check_emp import Check_emp_auth
from Response_messages.Messages import Success, UnAuthenticated, BadModel
from rest_framework import status
class Insert_Beeder(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            serializer = BeederSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                Success("Breeder","insert")
            else:
                BadModel("Inserting")
        else:
            return UnAuthenticated()
class Get_All_Breeder(APIView):
    def get(self,request):
        if Check_emp_auth(request) == True:
            all = Beeders.objects.all()
            serialized = BeederSerializer(all, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()

class Get_One_Breeder(APIView):
    def get(self,request, id):
        if Check_emp_auth(request) == True:
            breeder = Beeders.objects.filter(id=id).first()
            serialized = BeederSerializer(breeder)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()
class Update_Breeder(APIView):
    def post(self,request,id):
        if Check_emp_auth(request) == True:
            breeder = Beeders.objects.filter(id=id).first()
            serialized = BeederSerializer(instance=breeder,data=request.data)
            if serialized.is_valid():
                serialized.save()
                Success("Breeder","update")
            else:
                BadModel("Updating")
        else:
            UnAuthenticated()
class Delete_Breeder(APIView):
    def delete(self,request,id):
        if Check_emp_auth(request) == True:
            breeder = Beeders.objects.filter(id=id).first()
            breeder.delete()
            Success("Breeder","delete")
        else:
            UnAuthenticated()

"""Special query => Special class and fuction thet we want to filtering with differnt parameters in Breeder tabel"""