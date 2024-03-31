from rest_framework.response import Response
from rest_framework.views import APIView
from Policy.models import Policy
from Policy.serializer import PolicySerializer
from Authenticate.Check_emp import Emp_auth_checker
from Response_messages.Messages import Response_message
class AddPolicy(APIView,Emp_auth_checker,Response_message):
    def post(self,request):
        if self.Check_emp_auth(request) == True:
            policy = PolicySerializer(data=request.data)
            if policy.is_valid():
                policy.save()
                self.Success("Policy","insert")
            else:
                self.BadModel("Inserting")
        else:
            self.UnAuthenticated()
class UpdatePolicy(APIView,Emp_auth_checker,Response_message):
    def post(self,request,id):
        if self.Check_emp_auth(request) == True:
            policy = Policy.objects.filter(id=id).first()
            serializerd = PolicySerializer(date=policy,instance=request.data)
            if serializerd.is_valid():
                serializerd.save()
                self.Success("Policy","update")
            else:
                self.BadModel("Update")
        else:
            self.UnAuthenticated()
class DeletePolicy(APIView,Emp_auth_checker,Response_message):
    def delete(self,requset,id):
        if self.Check_emp_auth(requset) == True:
            policy = Policy.objects.filter(id=id).first()
            policy.delete()
            self.Success("Policy","delete")
        else:
            self.UnAuthenticated()