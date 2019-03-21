from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=40)
    lastlogin = models.DateTimeField(null=True, blank=True)
    point = models.IntegerField(default=0)
    class Meta:
        db_table = 'tb_myuser'

class UserToken(models.Model):
    """用户令牌"""
    token = models.CharField(max_length=32)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    class Meta:
        db_table = 'tb_token'



