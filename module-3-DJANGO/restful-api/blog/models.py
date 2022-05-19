from turtle import title
from django.conf import settings
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    donate = models.IntegerField(default = 0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self) -> str:
        return self.title