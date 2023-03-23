from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ArticleForm
from webapp.models import Article
from webapp.models.articles import StatusChoice


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'article_create.html', context={'choices': StatusChoice.choices, 'form': form})
    form = ArticleForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'article_create.html', context={'choices': StatusChoice.choices, 'form': form})
    else:
        article = Article.objects.create(**form.cleaned_data)
        return redirect('article_detail', pk=article.pk)


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', context={'article': article})


def update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
        return render(request, 'index.html', context={'form': form})

    form = ArticleForm(instance=article)
    return render(request, 'index.html', context={'form': form, 'article': article})


def delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_confirm_delete.html', context={'article': article})


def confirm_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')
