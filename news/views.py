from django.shortcuts import render
from django.views import generic
from news.models import New, Comment


# Create your views here.
def news(request):
    new = New.objects.all()
    return render(request, 'news.html', context={'news': new, })


def new_single(request, pk):
    new = New.objects.get(pk__exact=pk)
    comments = Comment.objects.filter(new__pk=new.pk)
    return render(request, 'new_single.html', context={'new': new, "comments": comments})


class NewListView(generic.ListView):
    model = New
