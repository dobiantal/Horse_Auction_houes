from rest_framework import serializers
from Employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'Fname',
            'Lname',
            'account_name',
            'email',
            'password',
            'Policy',
            'created_at',
            'updated_at',
            'deleted_at'
        )