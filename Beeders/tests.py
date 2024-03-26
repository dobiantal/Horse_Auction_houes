import datetime

from rest_framework import status
from rest_framework.test import APITestCase
from Policy.models import Policy
from Employee.models import Employee
from django.contrib.auth.hashers import make_password

class Insert_Breeder_TestCase(APITestCase):
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