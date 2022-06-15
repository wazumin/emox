from django.db import models
from django.conf import settings

# Create your models here.

class Comment(models.Model):
    emotion = models.CharField('感情', max_length=30)
    description = models.TextField('説明', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)

    created_at = models.DateTimeField("登校日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.emotion
