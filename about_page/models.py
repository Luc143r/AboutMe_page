from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(default='No description')
    link_project = models.URLField(max_length=200, default='Link missing')
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title