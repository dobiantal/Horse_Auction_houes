from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Horse
from .serializer import HorseSerializer, AllSerializer
from Authenticate.Check_emp import Check_emp_auth
from Authenticate.Check_bidder import Check_bidder_auth
from Response_messages.Messages import Success, UnAuthenticated, BadModel
class Add_Horse(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            serializerd = HorseSerializer(data=request.data)
            if serializerd.is_valid():
                serializerd.save()
                Success("Horse","insert")
            else:
                BadModel("Inserting")
        else:
            UnAuthenticated()
class Update_Horse(APIView):
    def post(self,request,id):
        if Check_emp_auth(request) == True:
            horse = Horse.objects().filter(id=id).first()
            serializerd = HorseSerializer(data=horse,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                Success("Horse","update")
            else:
                BadModel("Updating")
        else:
            UnAuthenticated()
class Delete_Horse(APIView):
    def delete(self,request,id):
        if Check_emp_auth(request) == True:
            horse = Horse.objects().filter(id=id).first()
            horse.delete()
            Success("Horse","delete")
        else:
            UnAuthenticated()
class Update_price(APIView):
    def post(self,request):
        if Check_bidder_auth(request) == True:
            actual_bid = Horse.objects().filter(id=request.data.get('id'))
            if int(actual_bid) >= request.data.get('bid'):
                return Response({"message":"To low bid. You have to take higher bid!"},status.HTTP_406_NOT_ACCEPTABLE)
            else:
                horse = Horse.object().filtered(id=request.data.get('id')).update(actual_price=request.data.get('bid'))
                serializered = HorseSerializer(horse)
                if serializered.is_valid():
                    serializered.save()
                    Success("Bid","update")
                else:
                    BadModel("Update bid")
        else:
            UnAuthenticated()
class Get_all_horse(APIView):
    def get(self,request):
        horses = Horse.objects.all()
        serializered = AllSerializer(horses, many=True)
        return Response(serializered.data,status.HTTP_200_OK)

class Get_only_OnBid(APIView):
    def get(self,request):
        if Check_bidder_auth(request) == True:
            onbid_horses = Horse.objects().filter(onbid=True).all()
            serializered = AllSerializer(onbid_horses, many=True)
            return Response(serializered.data,status.HTTP_200_OK)
        else:
            UnAuthenticated()