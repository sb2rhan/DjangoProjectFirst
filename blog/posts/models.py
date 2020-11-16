from django.db import models
# from django.contrib.auth.models import User # defaut Django user
from django.contrib.auth import get_user_model # function to get default Django user
from django.utils import timezone
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

    See user's posts:
    >> from django.contrib.auth.models import User
    >> u = User.objects.get(pk=1)
    >> u.post_set.all()
"""

class Post(models.Model):
    STATUS = [
        (1, 'published'),
        (0, 'unpublished')
    ]

    title = models.CharField(verbose_name='Название', max_length=120) # verbose_name is name in DB
    description = models.TextField(verbose_name='Описание', blank=True, default=None)
    publish_date = models.DateTimeField(verbose_name='Дата публикации', auto_now=timezone.now())
    status = models.CharField(verbose_name='Статус', max_length=190, choices=STATUS, default=1)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1) # model with this field is Many in relation Many to 1
    # CASCADE means posts will be deleted when user is deleted from DB

    tag = models.ManyToManyField('Tag') # now it does not show error and it is correct way
    # tag is gonna be QuerySet
    # Adding Tag to Post: >> post1.tag.add(tag1)

class Tag(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    slug = models.SlugField(verbose_name='Тематика', max_length=255, db_index=True)
    # slug is a link, db_index=True makes this field as index
