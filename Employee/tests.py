from rest_framework import status
from rest_framework.test import APITestCase



class EmpRegistrationTest(APITestCase):
    def RegTest(self,):
        data = {"Fname":"Test", "Lname":"Emp", "account_name":"teste", "email":"teste@gmail.com", "password":"12345",
                "policy_id":"1"}
        response = self.client.post("/api/emp_registrate" ,data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)