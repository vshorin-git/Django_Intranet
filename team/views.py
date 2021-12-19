import random
from datetime import date, timedelta

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from news.models import New, Comment
from .models import Employee, Role, City


def index(request):
    birthdays = []
    start = date.today()
    for delta_day in range(7):
        if Employee.objects.filter(birth_date__month=(start + timedelta(days=delta_day)).month,
                                   birth_date__day=(start + timedelta(days=delta_day)).day).count() > 0:
            birthdays.append(Employee.objects.filter(birth_date__month=(start + timedelta(days=delta_day)).month,
                                                     birth_date__day=(start + timedelta(days=delta_day)).day))
    context = {
        "birthdays": birthdays,
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
        random_male_first_name = random.choice(
            ['John', 'Bob', 'James', 'Robert', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles'])
        random_last_name = random.choice(
            ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez'])
        random_birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_role = random.choice(Role.objects.all())
        random_start_date = f"{random.randint(2019, 2020)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_phone = f"+{random.randint(10000000000, 99999999999)}"
        random_email = f"{random_male_first_name.lower()[0]}{random_last_name.lower()}@company.com"
        random_city = random.choice(City.objects.all())
        employee = Employee(first_name=random_male_first_name, last_name=random_last_name, sex="M",
                            birth_date=random_birth_date, start_date=random_start_date,
                            role=random_role, phone=random_phone, email=random_email, city=random_city)

        if Employee.objects.filter(first_name=random_male_first_name, last_name=random_last_name).count() == 0:
            employee.save()

    for i in range(10):
        random_female_first_name = random.choice(
            ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Isabella', 'Madison', 'Alexis', 'Hannah', 'Sarah'])
        random_last_name = random.choice(
            ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez'])
        random_birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_role = random.choice(Role.objects.all())
        random_start_date = f"{random.randint(2019, 2020)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        random_phone = f"+{random.randint(10000000000, 99999999999)}"
        random_email = f"{random_female_first_name.lower()[0]}{random_last_name.lower()}@company.com"
        random_city = random.choice(City.objects.all())
        employee = Employee(first_name=random_female_first_name, last_name=random_last_name, sex="F",
                            birth_date=random_birth_date, start_date=random_start_date,
                            role=random_role, phone=random_phone, email=random_email, city=random_city)
        if Employee.objects.filter(first_name=random_female_first_name, last_name=random_last_name).count() == 0:
            employee.save()

    for i in range(10):
        random_title = random.choice(
            ['Random title', 'Common title', 'Funny title', 'Scary title', 'Awful title', 'Clickbait title'])
        with open("D:\\MyPython\\Django_Intranet\\team\\loren_ipsum.txt", "r") as text:
            text2 = text.readlines()
            new_text = ""
            for line in text2[i * 5:i * 5 + 5]:
                new_text += line
        new_new = New(title=random_title, text=new_text)
        new_new.save()

    for i in range(100):
        random_text = random.choice(
            ['Random comment', 'Common comment', 'Funny comment', 'Scary comment', 'Awful comment',
             'Clickbait comment'])
        random_author = random.choice(Employee.objects.all())
        random_new = random.choice(New.objects.all())
        comment = Comment(new=random_new, text=random_text, author=random_author)
        comment.save()

    return HttpResponse('<a href="/"><h1>Initialization complete, go to the main page</h1></a>')
