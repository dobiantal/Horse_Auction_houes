from rest_framework.response import Response
from rest_framework.views import APIView
from Countries.models import Countries
from Countries.serializer import CountrySerializer
from Employee.views import EmpIsLogedIn
from Bidder.views import Bidder_isLoggedIn
class Insert_Country(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            serializered = CountrySerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                return Response({'message':'Inserting has been successful!'})
            else:
                return Response({'message':'Oops we have a problem! The inserting has been failed!'})
        else:
            return Response('Unauthenticated! Please login!')
class Update_Country(APIView):
    def post(self,request,id):
        if EmpIsLogedIn() == True:
            country = Countries.objects.filter(id=id).first()
            serialized = CountrySerializer(data=country,instance=request.data)
            if serialized.is_valid():
                serialized.save()
                return Response({'message': 'Updating has been successful!'})
            else:
                return Response({'message': 'Oops we have a problem! The updating has been failed!'})
        else:
            return Response('Unauthenticated! Please login!')
class Delete_Country(APIView):
    def delete(self,request,id):
        if EmpIsLogedIn() == True:
            country = Countries.objects.filter(id=id).first()
            country.delete()
            return Response({'message':'Delete has been successful!'})
        else:
            return Response('Unauthenticated! Please login!')
class Get_all_Countries(APIView):
    def get(self,request):
        if EmpIsLogedIn() == True or Bidder_isLoggedIn() == True:
            country = Countries.objects.all()
            serialized = CountrySerializer(country)
            return serialized
        else:
            return Response('Unauthenticated! Please login!')
class Get_one_Country(APIView):
    def get(self,request,id):
        if EmpIsLogedIn() == True or Bidder_isLoggedIn() == True:
            country = Countries.objects.filter(id=id).first()
            serialized = CountrySerializer(country)
            return serialized
        else:
            return Response('Unauthenticated! Please login!')