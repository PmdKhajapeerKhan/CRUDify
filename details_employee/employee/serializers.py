from rest_framework import serializers
from .models import Employee, EmployeeFinancialInfo

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'position']  # Specify only relevant fields

class EmployeeFinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeFinancialInfo
        fields = ['salary', 'bank_details', 'experience', 'account_number', 'ifsc_code']  # Specify only financial fields
