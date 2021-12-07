from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=20, help_text="Enter employee's first name")
    second_name = models.CharField(max_length=20, help_text="Enter employee's second name")
    sex = models.TextChoices('Sex', 'MALE FEMALE')
    birth_date = models.DateField(help_text="Choose employee's birth date")
    photo = models.ImageField()

    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    department = models.ForeignKey('Department', on_delete=models.PROTECT)
    start_date = models.DateField(help_text="Choose employee's start date in the company")
    manager = models.ForeignKey('self', on_delete=models.PROTECT)

    phone = PhoneNumberField()
    email = models.EmailField(max_length=40, help_text="Enter employee's email address")
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)

    description = models.CharField(max_length=2000, help_text="Enter additional info about employee")

    class Meta:
        ordering = ["second_name", "first_name"]

    def __str__(self):
        return f"Employee {self.second_name} {self.first_name} as {self.role} in {self.department}"

class Company(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    logo = models.ImageField()
    address = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=10)
    country = models.ForeignKey('Country', on_delete=models.PROTECT)

class Role(models.Model):
    name = models.CharField(max_length=50, help_text='Enter role in the company')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50, help_text="Enter company's department")

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50, help_text="Enter country name")

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50, help_text="Enter city name")

    def __str__(self):
        return self.name



