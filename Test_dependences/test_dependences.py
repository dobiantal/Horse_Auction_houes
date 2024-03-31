from Policy.models import Policy
from Employee.models import Employee
import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password
class TestDependences(APITestCase):
    def login_dependence(self):
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

