from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article, Tags


class NewsList(ListView):
    model = Article
    template_name = 'list.html'

    def get_context_data(self, *args, **kwargs):
        news_list = Article.objects.all()
        return {'news_list': news_list}


class TagsList(ListView):
    model = Tags
    template_name = 'tags_list.html'

    def get_context_data(self, *args, **kwargs):
        tags_list = Tags.objects.all()
        return {'tags_list': tags_list}


class NewsDetail(DetailView):
    model = Article
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        news_slug = self.get_slug_field()
        news = Article.objects.get(slug=news_slug)
        return {'news': news}