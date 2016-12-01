#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length = 30, unique = True, verbose_name = "Наименование категории")
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    def __unicode__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User, verbose_name = "Автор")
    category = models.ForeignKey(Category, verbose_name = "Категория")
    title = models.CharField(max_length = 150, verbose_name = "Заголовок")
    text = models.CharField(max_length = 1000, verbose_name = "Текст")
    creation_date = models.DateField(auto_now_add = True, verbose_name = "Дата создания поста")
    pub_date = models.DateTimeField(blank = True, null = True, verbose_name = "Дата и время публикации поста")
    last_change_date = models.DateField(auto_now = True, verbose_name = "Дата последнего изменеия поста")
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    def __unicode__(self):
        return self.category
