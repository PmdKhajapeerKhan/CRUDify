from django.urls import path
from .views import EmployeeList, EmployeeDetail, EmployeeFinancialInfoDetail

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:id>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees/<int:employee_id>/financial_info/', EmployeeFinancialInfoDetail.as_view(), name='employee_financial_info'),
]
