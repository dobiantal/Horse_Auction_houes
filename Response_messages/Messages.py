from rest_framework.response import Response
from rest_framework import status


def UnAuthenticated():
    return Response({"message":"UnAuthenticated! Please login"},status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

def BadModel(action:str):
    return Response({"message":f"{action} has been failed!"},status.HTTP_406_NOT_ACCEPTABLE)

def Success(model_name:str,action:str):
    return Response({"message": f"{model_name} {action} has been successful"}, status.HTTP_201_CREATED)
def NotFound(model_name: str):
    return Response({"message":f"{model_name} is not registered"},status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
def IncorretPW():
    return Response({"message":f"Incorrect password"},status.HTTP_400_BAD_REQUEST)