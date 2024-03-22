from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Horse
from .serializer import HorseSerializer, AllSerializer
from Employee.views import EmpIsLogedIn
from Bidder.views import Bidder_isLoggedIn
class Add_Horse(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            serializerd = HorseSerializer(data=request.data)
            if serializerd.is_valid():
                serializerd.save()
                return Response({'message':'Horse has been added!'})
            else:
                return Response({'message':'Horse adding has been failed'})
        else:
            Response({'message':'Unauthenticated! Please login!'})
class Update_Horse(APIView):
    def post(self,request,id):
        if EmpIsLogedIn() == True:
            horse = Horse.objects().filter(id=id).first()
            serializerd = HorseSerializer(data=horse,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                return Response({'message':'Uploading has been successful!'})
            else:
                return Response({'message':'Uploading has been failed!'})
        else:
            Response({'message': 'Unauthenticated! Please login!'})
class Delete_Horse(APIView):
    def delete(self,request,id):
        if EmpIsLogedIn() == True:
            horse = Horse.objects().filter(id=id).first()
            horse.delete()
            return Response({'message':'Delete has been successful!'})
        else:
            Response({'message': 'Unauthenticated! Please login!'})
class Update_price(APIView):
    def post(self,request):
        if Bidder_isLoggedIn() == True:
            horse = Horse.object().filtered(id=request.data.get('id')).update(actual_price=request.data.get('bid'))
            serializered = HorseSerializer(horse)
            if serializered.is_valid():
                serializered.save()
                return Response({'message':'Bid has been successful!'})
            else:
                return Response({'message':'Invalid bid! Please try again!'})
        else:
            Response({'message': 'Unauthenticated! Please login!'})
class Get_all_horse(APIView):
    def get(self,request):
        horses = Horse.objects.all()
        serializered = AllSerializer(horses, many=True)
        return Response(serializered.data)

class Get_only_OnBid(APIView):
    def get(self,request):
        if Bidder_isLoggedIn() == True:
            onbid_horses = Horse.objects().filter(onbid=True).all()
            serializered = AllSerializer(onbid_horses, many=True)
            return Response(serializered.data)
        else:
            Response({'message': 'Unauthenticated! Please login!'})