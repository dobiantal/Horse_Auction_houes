from rest_framework.response import Response
from rest_framework.views import APIView
from Policy.models import Policy
from Policy.serializer import PolicySerializer
from Employee.views import EmpIsLogedIn
class AddPolicy(APIView):
    def post(self,request):
        if EmpIsLogedIn() == True:
            policy = PolicySerializer(data=request.data)
            if policy.is_valid():
                policy.save()
                return Response({'message':'Policy has been added!'})
            else:
                return Response({'message': 'Policy adding has been failed!'})
        else:
            return Response({'message':'Unauthenticated! Please login!'})
class UpdatePolicy(APIView):
    def post(self,request,id):
        if EmpIsLogedIn() == True:
            policy = Policy.objects.filter(id=id).first()
            serializerd = PolicySerializer(date=policy,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                return Response({'message':'Policy has been updated!'})
            else:
                return Response({'message': 'Policy updating has been failed!'})
        else:
            return Response({'message':'Unauthenticated! Please login!'})
class DeletePolicy(APIView):
    def delete(self,requset,id):
        if EmpIsLogedIn() == True:
            policy = Policy.objects.filter(id=id).first()
            policy.delete()
            return Response({'message':'Policy has been deleted!'})
        else:
            return Response({'message':'Unauthenticated! Please login!'})