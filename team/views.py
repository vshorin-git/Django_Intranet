import random
from datetime import date, timedelta

from django.shortcuts import render

from news.models import New, Comment
from .models import Employee, Role
from django.db.models import Q, Sum


def index(request):
    start = date.today()
    start_day, start_month = start.day, start.month
    end = start + timedelta(days=15)
    end_day, end_month = end.day, end.month
    context = {
        "birthdays": Employee.objects.filter(Q(employee__birth_date__month=start_month,
    employee__birth_date__day__gt=start_day) | Q(employee__birth_date__month=end_month,employee__birth_date__day__lt=end_day)),
        "emp_count": Employee.objects.all().count(),
        "news_count": New.objects.all().count(),
        "comments_count": Comment.objects.all().count(),
        "role_count": Role.objects.all().count(),
        "departments_count": Role.objects.values('department').distinct().count(),
        "likes_count": New.objects.all().aggregate(Sum('likes'))["likes__sum"],
        "news": New.objects.order_by('-creation_date')[:5],
        }
    return render(request,'index.html',context=context)


def random_profile(request):
    user_profile = random.choice(Employee.objects.all())
    return render(request, 'profile.html', context={'user_profile': user_profile})


def profile(request):
    user_profile = random.choice(Employee.objects.all())
    return render(request, 'profile.html', context={'user_profile': user_profile})
