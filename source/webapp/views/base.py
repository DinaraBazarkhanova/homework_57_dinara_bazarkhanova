from django.shortcuts import render
from django.views import View

from webapp.forms import ArticleForm
from webapp.models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.exclude(is_deleted=True)
        context = {
            'articles': articles,
            'form': ArticleForm()
        }
        return render(request, 'index.html', context=context)


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         articles = Article.objects.exclude(is_deleted=True)
#         context = {
#             'articles': articles,
#             'form': ArticleForm()
#         }
#         return render(request, 'index.html', context=context)
