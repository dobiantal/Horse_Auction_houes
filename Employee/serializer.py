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
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    """In this method change the password to hash code."""
