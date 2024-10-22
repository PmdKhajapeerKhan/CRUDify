from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, EmployeeFinancialInfo
from .serializers import EmployeeSerializer, EmployeeFinancialInfoSerializer
from django.shortcuts import get_object_or_404
# from rest_framework.pagination import PageNumberPagination


class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    # def get(self, request):
    #     employees = Employee.objects.all()
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 10  # Set the number of items per page
    #     paginated_employees = paginator.paginate_queryset(employees, request)
    #     serializer = EmployeeSerializer(paginated_employees, many=True)
    #     return paginator.get_paginated_response(serializer.data)

    def post(self, request):

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """Delete an employee record."""
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeFinancialInfoDetail(APIView):
    def get(self, request, employee_id):
        financial_info = get_object_or_404(EmployeeFinancialInfo, employee_id=employee_id)
        serializer = EmployeeFinancialInfoSerializer(financial_info)
        return Response(serializer.data)

    def post(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeFinancialInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=employee)  # Associate financial info with employee
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, employee_id):
        financial_info = get_object_or_404(EmployeeFinancialInfo, employee_id=employee_id)
        serializer = EmployeeFinancialInfoSerializer(financial_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, employee_id):
        financial_info = get_object_or_404(EmployeeFinancialInfo, employee_id=employee_id)
        serializer = EmployeeFinancialInfoSerializer(financial_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, employee_id):
        financial_info = get_object_or_404(EmployeeFinancialInfo, employee_id=employee_id)
        financial_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

