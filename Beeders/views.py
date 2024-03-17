from rest_framework.response import Response
from rest_framework.views import APIView
from Beeders.serializer import BeederSerializer
from Beeders.models import Beeders
from Employee.views import EmpIsLogedIn
from Exceptions.projectExceptions import FailedInsertException, FailedUpdatingException
from rest_framework.exceptions import AuthenticationFailed
class Insert_Beeder(APIView):
    def post(self,request):
        if EmpIsLogedIn == True:
            serializer = BeederSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return {"message":"Breeder add has been successful"}
            else:
                raise FailedInsertException()
        else:
            raise AuthenticationFailed("UnAuthenticated! Please login")
class Get_All_Breeder(APIView):
    def get(self,request):
        if EmpIsLogedIn == True:
            all = Beeders.objects.all()
            serialized = BeederSerializer(all)
            return serialized.data
        else:
            raise AuthenticationFailed("UnAuthenticated! Please login")

class Get_One_Breeder(APIView):
    def get(self,request, id):
        if EmpIsLogedIn == True:
            breeder = Beeders.objects.filter(id=id).first()
            serialized = BeederSerializer(breeder)
            return serialized
        else:
            raise AuthenticationFailed("UnAuthenticated! Please login")
class Update_Breeder(APIView):
    def post(self,request,id):
        if EmpIsLogedIn == True:
            breeder = Beeders.objects.filter(id=id).first()
            serialized = BeederSerializer(instance=breeder,data=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response({"message":"Update has been successful!"})
            else:
                raise FailedUpdatingException()
        else:
            raise AuthenticationFailed("UnAuthenticated! Please login")
class Delete_Breeder(APIView):
    def delete(self,request,id):
        if EmpIsLogedIn == True:
            breeder = Beeders.objects.filter(id=id).first()
            breeder.delete()
            return Response({"message":"Breeder has been deleted!"})
        else:
            raise AuthenticationFailed("UnAuthenticated! Please login")

"""Special query => Special class and fuction thet we want to filtering with differnt parameters in Breeder tabel"""