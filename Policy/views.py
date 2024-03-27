from rest_framework.response import Response
from rest_framework.views import APIView
from Policy.models import Policy
from Policy.serializer import PolicySerializer
from Authenticate.Check_emp import Check_emp_auth
from Response_messages.Messages import Success, UnAuthenticated, BadModel
class AddPolicy(APIView):
    def post(self,request):
        if Check_emp_auth(request) == True:
            policy = PolicySerializer(data=request.data)
            if policy.is_valid():
                policy.save()
                Success("Policy","insert")
            else:
                BadModel("Inserting")
        else:
            UnAuthenticated()
class UpdatePolicy(APIView):
    def post(self,request,id):
        if Check_emp_auth(request) == True:
            policy = Policy.objects.filter(id=id).first()
            serializerd = PolicySerializer(date=policy,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                Success("Policy","update")
            else:
                BadModel("Update")
        else:
            UnAuthenticated()
class DeletePolicy(APIView):
    def delete(self,requset,id):
        if Check_emp_auth(requset) == True:
            policy = Policy.objects.filter(id=id).first()
            policy.delete()
            Success("Policy","delete")
        else:
            UnAuthenticated()