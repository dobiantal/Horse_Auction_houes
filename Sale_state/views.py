from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Sale_state
from .serializer import Sale_stateSerializer
from Authenticate.Check_emp import Emp_auth_checker
from Response_messages.Messages import Response_message
class Get_Sale_State(APIView):
    def get(self,request):
        sale_state = Sale_state.objects.all()
        serializered = Sale_stateSerializer(sale_state, many=True)
        return Response(serializered.data,status.HTTP_200_OK)
class Insert_sale_state(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            sale_state = Sale_stateSerializer(data=request.data)
            if sale_state.is_valid():
                sale_state.save()
                self.Success("Sale state","insert")
            else:
                self.BadModel("Inserting")
        else:
            self.UnAuthenticated()

class Upldate_sale_state(APIView,Emp_auth_checker,Response_message):
    def post(self,request,id):
        if self.Check_emp_auth(request) == True:
            sale_state = Sale_state.objects.filter(id=id).first()
            serializerd = Sale_stateSerializer(data=sale_state,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                self.Success("Sale state","update")
            else:
                self.BadModel("Updating")
        else:
            self.UnAuthenticated()
class Delete_sale_state(APIView,Emp_auth_checker,Response_message):
    def delete(self,request,id):
        if self.Check_emp_auth(request) == True:
            sale_state = Sale_state.objects.filter(id=id).first()
            sale_state.delete()
            self.Success("Sale state", "delete")
        else:
            self.UnAuthenticated()