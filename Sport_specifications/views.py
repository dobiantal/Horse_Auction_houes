from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sport_specification
from .serializer import Sport_specSerializer
from Employee.views import EmpIsLogedIn
class Get_Sport_spec(APIView):
    def get(self,request):
        sport_spec = Sport_specification.objects.all()
        serializered = Sport_specSerializer(sport_spec)
        return Response(serializered)
class Insert_sport_spec(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            serializered = Sport_specSerializer(data=request.data)
            if serializered.is_valid():
                serializered.save()
                return Response({'message':'Sport_spec has been added!'})
            else:
                return Response({'message':'Sport_spec insert has been failed'})
        else:
            return Response({'message':'Unauthenticated! Please login'})

