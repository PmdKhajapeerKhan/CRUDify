from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, EmployeeFinancialInfo
from .serializers import EmployeeSerializer, EmployeeFinancialInfoSerializer
# from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist

class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee = serializer.save()  # Save employee first
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    def get(self, request, id):
        employee = self.get_object(id)
        if employee is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, id):
        employee = self.get_object(id)
        if employee is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = self.get_object(id)
        if employee is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeFinancialInfoDetail(APIView):
    def get_object(self, employee_id):
        try:
            return EmployeeFinancialInfo.objects.get(employee_id=employee_id)
        except EmployeeFinancialInfo.DoesNotExist:
            return None

    def get(self, request, employee_id):
        financial_info = self.get_object(employee_id)
        if financial_info is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeFinancialInfoSerializer(financial_info)
        return Response(serializer.data)

    def post(self, request, employee_id):
        employee = Employee.objects.get(id=employee_id)
        serializer = EmployeeFinancialInfoSerializer(data=request.data)
        if serializer.is_valid():
            financial_info = serializer.save(employee=employee)  # Associate financial info with employee
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, employee_id):
        financial_info = self.get_object(employee_id)
        if financial_info is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeFinancialInfoSerializer(financial_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        financial_info = self.get_object(employee_id)
        if financial_info is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        financial_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
