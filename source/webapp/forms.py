from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'email', 'text', 'status')
        labels = {
            'name': 'Заголовок статьи',
            'email': 'Email',
            'text': 'Текст',
            'status': 'Статус'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError('Имя должно быть длинее 2 символов')
        return name
