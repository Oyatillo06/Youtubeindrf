from django.conf import settings
from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=70)
    video=models.URLField()
    description=models.TextField()

class Comment(models.Model):
    matn=models.TextField()
    account=models.ForeignKey(settings.ACCOUNT,on_delete=models.CASCADE,related_name='account_comment',null=True)
    sanasi=models.DateTimeField(auto_now_add=True)
    video=models.ForeignKey(settings.ACCOUNT,on_delete=models.CASCADE,related_name='account_video')

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    account = models.ForeignKey(settings.ACCOUNT, related_name='acc_video', on_delete=models.CASCADE)
    video = models.URLField()
    qoyilgan_kuni=models.CharField(max_length=40)

