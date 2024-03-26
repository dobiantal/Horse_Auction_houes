from rest_framework.response import Response
from rest_framework.views import APIView
from Authenticate.Check_emp import Check_emp_auth
from Cities.models import Cities
from Cities.serializer import CitySerializer
from Response_messages.Messages import Success, UnAuthenticated, BadModel
from rest_framework import status

class Insert_city(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            city = CitySerializer(data=request.data)
            if city.is_valid():
                city.save()
                Success("City","added")
            else:
                BadModel("Inserting")
        else:
            UnAuthenticated()
class Get_All_City(APIView):
    def get(self,request):
        if Check_emp_auth(request) == True:
            cities = Cities.objects.all()
            serialized = CitySerializer(cities, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()
class Get_One_City(APIView):
    def get(self,request, id):
        if Check_emp_auth(request) == True:
            city = Cities.objects.filter(id=id).first()
            serialized = CitySerializer(city)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()
class Update_City(APIView):
    def post(self,request,id):
        if Check_emp_auth(request) == True:
            city = Cities.objects.filter(id=id).first()
            serializerd = CitySerializer(data=city,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                Success("City","update")
            else:
                BadModel("Updating")
        else:
            UnAuthenticated()
class Delete_city(APIView):
    def delete(self,request,id):
        if Check_emp_auth(request) == True:
            city = Cities.objects.filter(id=id).first()
            city.delete()
            Success("City","delete")
        else:
            UnAuthenticated()
