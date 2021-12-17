import os, random

from team.models import *

def initial():
    roles = {'Marketing': 'Worker', 'Finance': 'Worker', 'IT': 'Worker', 'Product': 'Worker', 'Product': 'Manager',
             'Marketing': 'Manager', 'IT': 'Manager', 'Finance': 'Manager'}
    for key, value in cities.items():
        a = City(name=key, country=value)
        a.save()

    cities = {'Krasnodar':'Russia', 'Moscow':'Russia', 'New York':'USA', 'Los Angeles':'USA', 'Berlin':'Germany', 'London':'UK'}
    for key, value in cities.items():
        a=City(name=key,country=value)
        a.save()

    for i in range(10):
            random_male_first_names = random.choice(['John', 'Bob', 'James', 'Robert', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles'])
            random_male_second_names = random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez'])
            random_birth_date = f"{random.randint(1950, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 30):02d}"
            random_photo = random.choice(os.listdir("D:\MyPython\Django_Intranet\Male"))
            random_role = random.choice(Role.objects.all())
            random_start_date = f"{random.randint(2019,2020)}-{random.randint(1,12):02d}-{random.randint(1,30):02d}"
            random_phone =f"+{random.randint(10000000000,99999999999)}"
            random_email = f"{random_male_first_names.lower()[0]}{random_male_second_names.lower()}@company.com"
            random_city = random.choice(City.objects.all())
            employee = Employee(first_name=random_male_first_names, second_name=random_male_second_names, birth_date=random_birth_date, start_date=random_start_date, photo=random_photo, role=random_role, phone=random_phone, email=random_email, city=random_city)
            employee.save()






