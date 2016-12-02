from django.contrib import admin
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("creation_date", "category", "author", "title")
    search_fields = ("category", "author")
    date_hierarchy = 'creation_date'
    list_filter = ("author", "category",)
    list_editable = ("author", "title")

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
