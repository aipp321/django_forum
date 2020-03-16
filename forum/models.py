from django.db import models
from login.models import User
from datetime import date
# Create your models here.


class Text_type(models.Model):
    type_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.type_name

class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.TextField(default='none')
    c_time = models.DateTimeField('日期', default=date.today)
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(Text_type, on_delete=models.DO_NOTHING,default='无')

    def __str__(self):
        return self.title


