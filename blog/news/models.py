from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):

    title = models.CharField(verbose_name='Title', max_length=120)
    theme = models.CharField(verbose_name='Theme', max_length=100)
    publish_date = models.DateTimeField(verbose_name='Date of publish', auto_now=timezone.now())
    content = models.TextField(blank=False, null=False)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f'News: {self.title}, by {self.publisher}, {self.publish_date}'

    def get_absolute_url(self):
        return reverse("info", kwargs={"id": self.pk})
