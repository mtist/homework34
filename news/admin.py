from django.contrib import admin
from .models import Article, Tags

admin.site.register(Article)
admin.site.register(Tags)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
