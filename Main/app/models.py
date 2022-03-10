from django.db import models


class Post(models.Model):
    author = models.CharField('Автор поста', max_length=100)
    content = models.TextField('Содержимое комментария')
    create_date = models.DateTimeField(auto_now_add=True)


