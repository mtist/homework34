from django.views.generic.list import ListView
from .models import Article


class NewsList(ListView):
    model = Article
    template_name = 'list.html'

    def get_context_data(self, *args, **kwargs):
        news_list = Article.objects.all()
        return {'news_list': news_list}
