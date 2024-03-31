from rest_framework.response import Response
from rest_framework import status

class Response_message:
    def UnAuthenticated(self,):
        return Response({"message":"UnAuthenticated! Please login"},status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

    def BadModel(self,action:str):
        return Response({"message":f"{action} has been failed!"},status.HTTP_406_NOT_ACCEPTABLE)

    def Success(self,model_name:str,action:str):
        return Response({"message": f"{model_name} {action} has been successful"}, status.HTTP_201_CREATED)
    def NotFound(self,model_name: str):
        return Response({"message":f"{model_name} is not registered"},status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
    def IncorretPW(self,):
        return Response({"message":f"Incorrect password"},status.HTTP_400_BAD_REQUEST)