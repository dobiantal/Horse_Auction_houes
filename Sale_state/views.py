from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sale_state
from .serializer import Sale_stateSerializer
from Employee.views import EmpIsLogedIn
class Get_Sale_State(APIView):

    def get(self,request):
        sale_state = Sale_state.objects.all()
        serializered = Sale_stateSerializer(sale_state, many=True)
        return Response(serializered.data)
class Insert_sale_state(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            sale_state = Sale_stateSerializer(data=request.data)
            if sale_state.is_valid():
                sale_state.save()
                return Response({'message':'New state has been created!'})
            else:
                return Response({'message':'Invalid inputs'})
        else:
            return Response('Unauthenticated! Please login')

class Upldate_sale_state(APIView):
    def post(self,request,id):
        if EmpIsLogedIn() == True:
            sale_state = Sale_state.objects.filter(id=id).first()
            serializerd = Sale_stateSerializer(data=sale_state,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                return Response({'message':'State upload has been successful!'})
class Delete_sale_state(APIView):
    def delete(self,request,id):
        if EmpIsLogedIn() == True:
            sale_state = Sale_state.objects.filter(id=id).first()
            sale_state.delete()
            return Response({'message':'State delete has been successful'})
        else:
            return Response('Unauthenticated! Please login')