from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from Cities.models import Cities
from Cities.serializer import CitySerializer
from Exceptions.projectExceptions import FailedInsertException, FailedUpdatingException, FailedDeleteexception
from Employee.views import EmpIsLogedIn

class Insert_city(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            city = CitySerializer(data=request.data)
            if city.is_valid():
                city.save()
                return Response({"message":"City add has been successful!"})
            else:
                raise FailedInsertException()
class Get_All_City(APIView):
    def get(self,request):
        if EmpIsLogedIn() == True:
            cities = Cities.objects.all()
            serialized = CitySerializer(cities)
            return serialized.data
        else:
            raise AuthenticationFailed("Unauthenticated! Please login!")
class Get_One_City(APIView):
    def get(self,request, id):
        if EmpIsLogedIn() == True:
            city = Cities.objects.filter(id=id).first()
            serialized = CitySerializer(city)
            return serialized.data
        else:
            raise AuthenticationFailed("Unauthenticated! Please login!")
class Update_City(APIView):
    def post(self,request,id):
        city = Cities.objects.filter(id=id).first()
        serializerd = CitySerializer(data=city,instance=request.data)
        if serializerd.is_valid():
            serializerd.save()
            return Response({"message":"Update has been successful!!"})
        else:
            raise FailedUpdatingException()
class Delete_city(APIView):
    def delete(self,request,id):
        if EmpIsLogedIn() == True:
            city = Cities.objects.filter(id=id).first()
            city.delete()
            return Response({"message":"Delete has been successful!!"})
        else:
            raise FailedDeleteexception()