from django.db import models
# Create your models here.
class BlogsPost(models.Model):
    title=models.CharField(max_length=150)
    keyword1=models.CharField(max_length=50,default="")
    body=models.TextField()
    timestamp=models.DateTimeField('保存日期')
