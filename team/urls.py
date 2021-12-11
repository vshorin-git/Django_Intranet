from django.urls import path, re_path

from . import views as teamv
from news import views as newsv

urlpatterns = [
    path('', teamv.index, name='index'),
    path('profile/', teamv.random_profile, name='random_profile'),
    path('profile/<employee_email>', teamv.profile, name='profile'),
    path('news/', newsv.news, name='news'),
    # re_path(r'^team/$', teamv.Employee.as_view(), name='team')
    ]