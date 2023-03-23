from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.forms import ArticleForm
from webapp.models import Article


def index_view(request: WSGIRequest):
    articles = Article.objects.exclude(is_deleted=True)
    context = {
        'articles': articles,
        'form': ArticleForm()
    }
    return render(request, 'index.html', context=context)
