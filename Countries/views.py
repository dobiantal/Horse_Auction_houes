from rest_framework.response import Response
from rest_framework.views import APIView
from Countries.models import Countries
from Countries.serializer import CountrySerializer
from Authenticate.Check_emp import Emp_auth_checker
from Authenticate.Check_bidder import Bidder_auth_checker
from Response_messages.Messages import Response_message
from rest_framework import status
class Insert_Country(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            serializered = CountrySerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                self.Success("Country","added")
            else:
                self.BadModel("Inserting")
        else:
            self.UnAuthenticated()
class Update_Country(APIView,Emp_auth_checker,Response_message):
    def post(self,request,id):
        if self.Check_emp_auth(request) == True:
            country = Countries.objects.filter(id=id).first()
            serialized = CountrySerializer(data=country,instance=request.data)
            if serialized.is_valid():
                serialized.save()
                self.Success("Country","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_Country(APIView,Emp_auth_checker,Response_message):
    def delete(self,request,id):
        if self.Check_emp_auth(request) == True:
            country = Countries.objects.filter(id=id).first()
            country.delete()
            self.Success("Country","delete")
        else:
            self.UnAuthenticated()
class Get_all_Countries(APIView,Emp_auth_checker,Bidder_auth_checker,Response_message):
    def get(self,request):
        if self.Check_emp_auth(request) == True or self.Check_bidder_auth(request) == True:
            country = Countries.objects.all()
            serialized = CountrySerializer(country, many=True)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()
class Get_one_Country(APIView,Emp_auth_checker,Bidder_auth_checker,Response_message):
    def get(self,request,id):
        if self.Check_emp_auth(request) == True or self.Check_bidder_auth(request) == True:
            country = Countries.objects.filter(id=id).first()
            serialized = CountrySerializer(country)
            return Response(serialized.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()