from django.db import models

# Create your models here.

class UserRank(models.Model):

    agent = models.CharField(max_length=64,verbose_name='客户端名称')
    score = models.IntegerField(verbose_name='客户端分数')
    objects = models.Manager()
    class Meta:
        verbose_name_plural = '用户分数表'
        db_table = 'userrank'

