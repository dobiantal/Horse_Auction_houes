from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from Employee.models import Employee
from Policy.serializer import PolicySerializer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.password = make_password(password)
            instance.save()
        return instance
    """In this method change the password to hash code."""
class EmpInnerJoinSerializer(serializers.ModelSerializer):
    policy_id = PolicySerializer(many=True)
    class Meta:
        model = Employee
        fields = '__all__'