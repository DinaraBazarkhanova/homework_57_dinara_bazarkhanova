# Generated by Django 4.1.6 on 2023-03-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('text', models.TextField(max_length=200, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=20, verbose_name='Статус')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Дата и время удаления')),
            ],
        ),
    ]
