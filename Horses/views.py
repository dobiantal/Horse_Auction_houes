from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Horse
from .serializer import HorseSerializer, AllSerializer

from Authenticate.Check_emp import Emp_auth_checker
from Authenticate.Check_bidder import Bidder_auth_checker
from Response_messages.Messages import Response_message

class Add_Horse(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            serializerd = HorseSerializer(data=request.data)
            if serializerd.is_valid():
                serializerd.save()
                self.Success("Horse","insert")
            else:
                self.BadModel("Inserting")
        else:
            self.UnAuthenticated()
class Update_Horse(APIView,Emp_auth_checker,Response_message):
    def post(self,request,id):
        if self.Check_emp_auth(request) == True:
            horse = Horse.objects().filter(id=id).first()
            serializerd = HorseSerializer(data=horse,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                self.Success("Horse","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_Horse(APIView,Emp_auth_checker,Response_message):
    def delete(self,request,id):
        if self.Check_emp_auth(request) == True:
            horse = Horse.objects().filter(id=id).first()
            horse.delete()
            self.Success("Horse","delete")
        else:
            self.UnAuthenticated()
class Update_price(APIView,Bidder_auth_checker,Response_message):
    def post(self,request):
        if self.Check_bidder_auth(request) == True:
            actual_bid = Horse.objects().filter(id=request.data.get('id'))
            if int(actual_bid) >= request.data.get('bid'):
                return Response({"message":"To low bid. You have to take higher bid!"},status.HTTP_406_NOT_ACCEPTABLE)
            else:
                horse = Horse.object().filtered(id=request.data.get('id')).update(actual_price=request.data.get('bid'))
                serializered = HorseSerializer(horse)
                if serializered.is_valid():
                    serializered.save()
                    self.Success("Bid","update")
                else:
                    self.BadModel("Update bid")
        else:
            self.UnAuthenticated()
class Get_all_horse(APIView):
    def get(self,request):
        horses = Horse.objects.all()
        serializered = AllSerializer(horses, many=True)
        return Response(serializered.data,status.HTTP_200_OK)

class Get_only_OnBid(APIView,Bidder_auth_checker,Response_message):
    def get(self,request):
        if self.Check_bidder_auth(request) == True:
            onbid_horses = Horse.objects().filter(onbid=True).all()
            serializered = AllSerializer(onbid_horses, many=True)
            return Response(serializered.data,status.HTTP_200_OK)
        else:
            self.UnAuthenticated()
