from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Tags(models.Model):
    title = models.CharField('Тег', max_length=16)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=32)
    slug = models.SlugField(max_length=32)
    date = models.DateField(auto_now=True)
    img = models.ImageField('Фото', default='.static/photo.png', blank=True)
    # content = RichTextUploadingField(default='')
    content = models.TextField('text')
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title
