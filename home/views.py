from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
# pages/views.py
from django.views.generic import TemplateView
from lots.models import Article
from . import views
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from lots.filters import ArticleFilter


def index(request):
    bbs = Article.objects.filter(status=True)

    myHomeFilter = ArticleFilter(request.GET, queryset=Article.objects.all())
    bbs = myHomeFilter.qs

    paginator = Paginator(bbs, 4)
    page = request.GET.get('page')
    try:
        bbs = paginator.page(page)
    except PageNotAnInteger:
        bbs = paginator.page(1)
    except EmptyPage:
        bbs = paginator.page(paginator.num_pages)

    context = {'bbs': bbs, 'myHomeFilter': myHomeFilter}
    return render(request, 'index.html', context)
