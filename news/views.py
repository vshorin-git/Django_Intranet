from django.shortcuts import render
from django.views import generic
from news.models import New, Comment


# Create your views here.
def news(request):
    new = New.objects.all()
    return render(request, 'news.html', context={'news': new, })


def new_single(request, pk):
    new = New.objects.get(pk__exact=pk)
    print(f"{new.title} - {new.text}")
    return render(request, 'new_single.html', context={'news': new, })


class NewListView(generic.ListView):
    model = New
