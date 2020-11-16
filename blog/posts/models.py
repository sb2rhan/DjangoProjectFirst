from django.db import models

# Create your models here.
"""
    Command that saves model in db by shell:
    > python manage.py shell
    >> from post.models import Post
    >> Post(title='s', description='text').save()

    Another option(More Django way):
    > python manage.py shell
    >> from post.models import Post
    >> post = Post.objects.create(title='ORM', description='O')

    Get all models:
    >> from post.models import Post
    >> Post.objects.all()
    Get 1 model
    >> Post.objects.get(id=1) # .get(pk=1)

    Change model
    >> from post.models import Post
    >> post = Post.objects.get(pk=1)
    >> post.title = 'another'
    >> post.save()
"""

class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=120) # verbose_name is name in DB
    description = models.TextField(verbose_name='Описание', blank=True, default=None)
    # publish_date = models.DateTimeField(verbose_name='Дата публикации', null=True)
