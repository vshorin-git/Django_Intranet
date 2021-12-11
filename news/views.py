from django.shortcuts import render

from news.models import New, Comment


# Create your views here.
def news(request):
    news = New.objects.all()
    return render(request,'news.html',context={'news':news,})