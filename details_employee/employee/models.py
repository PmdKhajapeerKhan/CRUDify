from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=225)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeFinancialInfo(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='financial_info')
    bank_details = models.CharField(max_length=225)
    account_number = models.BigIntegerField(default='0000000000')
    ifsc_code = models.CharField(max_length=100)  # New field for bank details
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # New field for salary
    experience = models.IntegerField()  # New field for experience in years

    def __str__(self):
        return f"Financial Info for {self.employee.first_name} {self.employee.last_name}"
