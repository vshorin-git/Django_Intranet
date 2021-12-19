from django.db import models
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=20, help_text="Enter employee's first name")
    last_name = models.CharField(max_length=20, help_text="Enter employee's second name")
    M = "M"
    F = "F"
    SEX_CHOICES = [(M, 'Male'), (F, 'Female')]
    sex = models.CharField(max_length=1,choices=SEX_CHOICES, default=M,)
    birth_date = models.DateField(help_text="Choose employee's birth date")
    photo = models.ImageField(blank=True)

    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    start_date = models.DateField(help_text="Choose employee's start date in the company")
    manager = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    mailing_groups = models.ManyToManyField('MailingGroup',blank=True)

    phone = models.CharField(max_length=15, help_text="Enter employee's phone number")
    email = models.EmailField(max_length=40, help_text="Enter employee's email address", )
    city = models.ForeignKey('City', on_delete=models.PROTECT)

    description = models.CharField(max_length=2000, help_text="Enter additional info about employee", blank=True)
    is_fired = models.BooleanField(default=False)
    firing_date = models.DateField(help_text="Choose employee's firing date in the company", blank=True, null=True)
    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse('profile', args=(self.email,))



class Company(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    logo = models.ImageField()
    address = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.PROTECT)
    zip_code = models.CharField(max_length=10)

class Role(models.Model):
    role = models.CharField(max_length=50, help_text='Enter role in the company')
    department = models.CharField(max_length=50, help_text="Enter company's department")

    def __str__(self):
        return f"{self.department} department, {self.role}"


class City(models.Model):
    name = models.CharField(max_length=50, help_text="Enter city name")
    country = models.CharField(max_length=50, help_text="Enter country name")

    def __str__(self):
        return self.name

class MailingGroup(models.Model):
    mail_group = models.CharField(max_length=50, help_text="Enter mailing group name")

    def __str__(self):
        return self.mail_group



