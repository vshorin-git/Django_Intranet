from django.shortcuts import render
from django.views import generic
from news.models import New, Comment
from django.core.paginator import Paginator


# Create your views here.
def news(request):
    news = New.objects.all()
    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', context={'page_obj': page_obj, })


def new_single(request, pk):
    new = New.objects.get(pk__exact=pk)
    comments = Comment.objects.filter(new__pk=new.pk)
    return render(request, 'new_single.html', context={'new': new, "comments": comments})


class NewListView(generic.ListView):
    model = New
