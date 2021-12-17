from django.urls import path, re_path

from . import views as teamv
from news import views as newsv

urlpatterns = [
    path('', teamv.index, name='index'),
    path('profile/random', teamv.random_profile, name='random_profile'),
    path('profile/<email>', teamv.profile, name='profile'),
    path('news/<pk>', newsv.new_single, name='new_single'),
    path('news/', newsv.news, name='news'),
    re_path(r'^team/$', teamv.EmployeeListView.as_view(), name='team'),
    # re_path(r'^news/$', newsv.NewListView.as_view(), name='news_single'),
    path('initialize/', teamv.initialize, name='initialize'),
    ]