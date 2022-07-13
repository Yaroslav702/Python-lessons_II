from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    category = models.ManyToManyField(Category)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    donate = models.IntegerField(default = 0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def set_like(self):
        self.likes += 1
        self.save()

    def set_dislike(self):
        self.dislikes += 1
        self.save()

    def __gt__(self, other):
        return self.donate > other.donate

    
    def __str__(self) -> str:
        return self.title


