from rest_framework.response import Response
from rest_framework.views import APIView
from Beeders.serializer import BeederSerializer
from Beeders.models import Beeders
from Authenticate.Check_emp import Emp_auth_checker
from Response_messages.Messages import Response_message
from rest_framework import status
class Insert_Beeder(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            serializer = BeederSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                self.Success("Breeder","insert")
            else:
                self.BadModel("Inserting")
        else:
            return self.UnAuthenticated()
class Get_All_Breeder(APIView,Emp_auth_checker,Response_message):
    def get(self,request):
        if self.Check_emp_auth(request) == True:
            all = Beeders.objects.all()
            serialized = BeederSerializer(all, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()

class Get_One_Breeder(APIView,Emp_auth_checker,Response_message):
    def get(self,request, id):
        if self.Check_emp_auth(request) == True:
            breeder = Beeders.objects.filter(id=id).first()
            serialized = BeederSerializer(breeder)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()
class Update_Breeder(APIView,Emp_auth_checker,Response_message):
    def post(self,request,id):
        if self.Check_emp_auth(request) == True:
            breeder = Beeders.objects.filter(id=id).first()
            serialized = BeederSerializer(instance=breeder,data=request.data)
            if serialized.is_valid():
                serialized.save()
                self.Success("Breeder","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_Breeder(APIView,Emp_auth_checker,Response_message):
    def delete(self,request,id):
        if self.Check_emp_auth(request) == True:
            breeder = Beeders.objects.filter(id=id).first()
            breeder.delete()
            self.Success("Breeder","delete")
        else:
            self.UnAuthenticated()

"""Special query => Special class and fuction thet we want to filtering with differnt parameters in Breeder tabel"""