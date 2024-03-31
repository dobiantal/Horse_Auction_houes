from rest_framework.response import Response
from rest_framework.views import APIView
from Authenticate.Check_emp import Emp_auth_checker
from Cities.models import Cities
from Cities.serializer import CitySerializer
from Response_messages.Messages import Response_message
from rest_framework import status

class Insert_city(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            city = CitySerializer(data=request.data)
            if city.is_valid():
                city.save()
                self.Success("City","added")
            else:
                self.BadModel("Inserting")
        else:
            self.UnAuthenticated()
class Get_All_City(APIView,Emp_auth_checker,Response_message):
    def get(self,request):
        if self.Check_emp_auth(request) == True:
            cities = Cities.objects.all()
            serialized = CitySerializer(cities, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()
class Get_One_City(APIView,Emp_auth_checker,Response_message):
    def get(self,request, id):
        if self.Check_emp_auth(request) == True:
            city = Cities.objects.filter(id=id).first()
            serialized = CitySerializer(city)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()
class Update_City(APIView,Emp_auth_checker,Response_message):
    def post(self,request,id):
        if self.Check_emp_auth(request) == True:
            city = Cities.objects.filter(id=id).first()
            serializerd = CitySerializer(data=city,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                self.Success("City","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_city(APIView,Emp_auth_checker,Response_message):
    def delete(self,request,id):
        if self.Check_emp_auth(request) == True:
            city = Cities.objects.filter(id=id).first()
            city.delete()
            self.Success("City","delete")
        else:
            self.UnAuthenticated()