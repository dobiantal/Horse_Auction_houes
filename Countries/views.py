from rest_framework.response import Response
from rest_framework.views import APIView
from Countries.models import Countries
from Countries.serializer import CountrySerializer
from Employee.views import EmpIsLogedIn
from Authenticate.Check_emp import Check_emp_auth
from Authenticate.Check_bidder import Check_bidder_auth
from Response_messages.Messages import UnAuthenticated, Success, BadModel
from rest_framework import status
class Insert_Country(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            serializered = CountrySerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                Success("Country","added")
            else:
                BadModel("Inserting")
        else:
            UnAuthenticated()
class Update_Country(APIView):
    def post(self,request,id):
        if Check_emp_auth(request) == True:
            country = Countries.objects.filter(id=id).first()
            serialized = CountrySerializer(data=country,instance=request.data)
            if serialized.is_valid():
                serialized.save()
                Success("Country","update")
            else:
                BadModel("Updating")
        else:
            UnAuthenticated()
class Delete_Country(APIView):
    def delete(self,request,id):
        if Check_emp_auth(request) == True:
            country = Countries.objects.filter(id=id).first()
            country.delete()
            Success("Country","delete")
        else:
            UnAuthenticated()
class Get_all_Countries(APIView):
    def get(self,request):
        if Check_emp_auth(request) == True or Check_bidder_auth(request) == True:
            country = Countries.objects.all()
            serialized = CountrySerializer(country, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()
class Get_one_Country(APIView):
    def get(self,request,id):
        if Check_emp_auth(request) == True or Check_bidder_auth(request) == True:
            country = Countries.objects.filter(id=id).first()
            serialized = CountrySerializer(country)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()