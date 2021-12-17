import os
import random
from datetime import date, timedelta, datetime
from django.http import HttpResponse

from django.db.models import Q, Sum
from django.shortcuts import render
from django.views import generic

from news.models import New, Comment
from .models import Employee, Role, City


def index(request):
    start = date.today()
    start_day, start_month = start.day, start.month
    end = start + timedelta(days=15)
    end_day, end_month = end.day, end.month
    context = {
        "birthdays": Employee.objects.filter(Q(employee__birth_date__month=start_month,
                                               employee__birth_date__day__gt=start_day) | Q(
            employee__birth_date__month=end_month, employee__birth_date__day__lt=end_day)),
        "emp_count": Employee.objects.all().count(),
        "news_count": New.objects.all().count(),
        "comments_count": Comment.objects.all().count(),
        "role_count": Role.objects.all().count(),
        "departments_count": Role.objects.values('department').distinct().count(),
        "likes_count": New.objects.all().aggregate(Sum('likes'))["likes__sum"],
        "news": New.objects.order_by('-creation_date')[:3],
    }
    return render(request, 'index.html', context=context)


def random_profile(request):
    user_profile = random.choice(Employee.objects.all())
    return render(request, 'profile.html', context={'user_profile': user_profile})


def profile(request, email):
    user_profile = Employee.objects.get(email__exact=email)
    return render(request, 'profile.html', context={'user_profile': user_profile})


class EmployeeListView(generic.ListView):
    model = Employee


def initialize(request):
    roles = {'Marketing': 'Worker', 'Finance': 'Worker', 'IT': 'Worker', 'Product': 'Worker', 'Product': 'Manager',
             'Marketing': 'Manager', 'IT': 'Manager', 'Finance': 'Manager'}
    for key, value in roles.items():
        role = Role(department=key, role=value)
        role.save()

    cities = {'Krasnodar': 'Russia', 'Moscow': 'Russia', 'New York': 'USA', 'Los Angeles': 'USA', 'Berlin': 'Germany',
              'London': 'UK'}
    for key, value in cities.items():
        city = City(name=key, country=value)
        city.save()

    for i in range(10):
        random_male_first_names = random.choice(
            ['John', 'Bob', 'James', 'Robert', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles'])
        random_male_last_names = random.choice(
            ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez'])
        random_birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_photo = random.choice(os.listdir("D:\\MyPython\\Django_Intranet\\team\static\\"))
        random_role = random.choice(Role.objects.all())
        random_start_date = f"{random.randint(2019, 2020)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_phone = f"+{random.randint(10000000000, 99999999999)}"
        random_email = f"{random_male_first_names.lower()[0]}{random_male_last_names.lower()}@company.com"
        random_city = random.choice(City.objects.all())
        employee = Employee(first_name=random_male_first_names, last_name=random_male_last_names, sex="M",
                            birth_date=random_birth_date, start_date=random_start_date, photo=random_photo,
                            role=random_role, phone=random_phone, email=random_email, city=random_city)
        employee.save()

    for i in range(10):
        random_male_first_names = random.choice(
            ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Isabella', 'Madison', 'Alexis', 'Hannah', 'Sarah'])
        random_male_last_names = random.choice(
            ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez'])
        random_birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_photo = random.choice(os.listdir("D:\\MyPython\\Django_Intranet\\team\\static\\"))
        random_role = random.choice(Role.objects.all())
        random_start_date = f"{random.randint(2019, 2020)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_phone = f"+{random.randint(10000000000, 99999999999)}"
        random_email = f"{random_male_first_names.lower()[0]}{random_male_last_names.lower()}@company.com"
        random_city = random.choice(City.objects.all())
        employee = Employee(first_name=random_male_first_names, last_name=random_male_last_names, sex="F",
                            birth_date=random_birth_date, start_date=random_start_date, photo=random_photo,
                            role=random_role, phone=random_phone, email=random_email, city=random_city)
        employee.save()


    for i in range(10):
        random_title = random.choice(
            ['Random title', 'Common title', 'Funny title', 'Scary title', 'Awful title', 'Clickbait title'])
        with open("D:\\MyPython\\Django_Intranet\\team\\loren_ipsum.txt", "r") as text:
            text2 = text.readlines()
            new_text = ""
            for line in text2[i*5:i*5+5]:
                new_text += line
        new_new = New(title=random_title, text=new_text)
        new_new.save()

    for i in range(100):
        random_text = random.choice(
            ['Random comment', 'Common comment', 'Funny comment', 'Scary comment', 'Awful comment', 'Clickbait comment'])
        random_author = random.choice(Employee.objects.all())
        random_new = random.choice(New.objects.all())
        comment = Comment(new=random_new,text=random_text, author=random_author)
        comment.save()

    return HttpResponse('<a href="/"><h1>Initialization complete, go to the main page</h1></a>')
