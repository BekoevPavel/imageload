

from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect



#def index(request):

   # latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    #return render(request, 'article/list.html',{'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена")


    return render(request,'article/detail.html',{'article':a})




