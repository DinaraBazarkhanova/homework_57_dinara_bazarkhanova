from django.urls import path

from webapp.views.articles import add_view, update_view, delete_view, confirm_delete, detail_view
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('article/', IndexView.as_view()),
    path('article/add/', add_view, name='article_add'),
    path('article/<int:pk>', detail_view, name='article_detail'),
    path('article/<int:pk>/update', update_view, name='article_update'),
    path('article/<int:pk>/delete', delete_view, name='article_delete'),
    path('article/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete'),
]
