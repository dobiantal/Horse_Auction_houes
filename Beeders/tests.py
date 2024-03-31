import datetime

from rest_framework import status
from rest_framework.test import APITestCase
from Policy.models import Policy
from Employee.models import Employee
from Beeders.models import Beeders
from django.contrib.auth.hashers import make_password
from Test_dependences.test_dependences import TestDependences
class Insert_Breeder_TestCases(APITestCase):
    def dependence(self):
        # Dependence method. It is providing login procedure with employee
        policy = Policy(id=1, policy="Assistant")
        policy.save()
        assistant = Policy.objects.filter(id=1).first()
        employee = Employee(id=1,
                            Fname="Dobi",
                            Lname="Antal",
                            account_name="dobia",
                            email="antal.dobi.93@gmail.com",
                            password=make_password("12345"),
                            policy_id=assistant,
                            created_at=datetime.datetime.utcnow(),
                            updated_at=datetime.datetime.utcnow()
                            )
        employee.save()
        login = {
            "account_name": "dobia",
            "password": '12345'
        }
        response = self.client.post("/api/emp_login", login)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    def test_insert1(self):
        #I have been checked add breeder method is valid.
        self.dependence()
        data = {"Beeder_F_name":"James", "Beeder_L_name":"Elder", "Stable_name":"Sunshine", "Beeder_phone":"+225346456",
                "Beeder_email":"ElderJ@il.com", "Beeder_webpage":"sunny.horses.com"}
        response = self.client.post("/api/breeder_reg", data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_insert2(self):
        # I have been checked the serializer method if the data are invalid.
        self.dependence()
        data = {"Beeder_F_name":"James", "Beeder_L_name":"Elder", "Stable_name":"Sunshine", "Beeder_phone":"+225346456",
                "Beeder_email":"ElderJ@il.com", "Beederwebpage":"sunny.horses.com"}
        response = self.client.post("/api/breeder_reg", data)
        self.assertEquals(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

    def test_insert3(self):
        data = {"Beeder_F_name": "James", "Beeder_L_name": "Elder", "Stable_name": "Sunshine",
                "Beeder_phone": "+225346456",
                "Beeder_email": "ElderJ@il.com", "Beederwebpage": "sunny.horses.com"}
        response = self.client.post("/api/breeder_reg", data)
        self.assertEquals(response.status_code, status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)

"""class Breeder_Getter_Cases(APITestCase):
    def test_getter1(self,):
        dependences = TestDependences()
        dependences.login_dependence()
        # This test is checks we can get all breeder form the server
        response = self.client.post("/api/breeder_all")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    def test_getter2(self):
        #This test checks if we didn't authenticate ourselves then return an unauthenticated message.
        response = self.client.post("/api/breeder_all")
        self.assertEquals(response.status_code, status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
    def test_getter3(self):
        #This test checks we can get one bidder data from the server
        dependences = TestDependences()
        dependences.login_dependence()
        response = self.client.post("/api/breeder_one/1")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    def test_getter4(self):
        #This test is checks if we didn't authenticate response 407
        response = self.client.post("/api/breeder_one/1")
        self.assertEquals(response.status_code, status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED)
    def test_update1(self):
         This test is checks we can update data in Breeder model. I will modify the Breeder_F_name, Breeder_webpage
        from James to Frank and the webpage address from sunny to windy.
        
        dependences = TestDependences()
        dependences.login_dependence()
        pattern = Beeders(id=1,
                         Beeder_F_name= "James",
                         Beeder_L_name= "Elder",
                         Stable_name= "Sunshine",
                         Beeder_phone= "+225346456",
                         Beeder_email= "ElderJ@il.com",
                         Beeder_webpage= "sunny.horses.com")
        pattern.save()
        data = {"Beeder_F_name": "Frank", "Beeder_L_name": "Elder", "Stable_name": "Sunshine",
                "Beeder_phone": "+225346456",
                "Beeder_email": "ElderJ@il.com", "Beeder_webpage": "windy.horses.com"}
        response = self.client.post("api/breeder_update/1", data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        updated_model = Beeders.objects().filter(id=1).values('Beeder_F_name','Beeder_webpage')
        self.assertEquals(updated_model.Beeder_F_name, "Frank")
        self.assertEquals(updated_model.Beeder_webpage,"windy.horses.com")
    def test_update2(self):
        #This test is checks the authentication has done.
        data = {"Beeder_F_name": "Frank", "Beeder_L_name": "Elder", "Stable_name": "Sunshine",
                "Beeder_phone": "+225346456",
                "Beeder_email": "ElderJ@il.com", "Beeder_webpage": "windy.horses.com"}
        response = self.client.post("api/breeder_update/1", data)
        self.assertEquals(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)"""