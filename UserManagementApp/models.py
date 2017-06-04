from django.db import models

class UserLoginDatetime(models.Model):
    user_name = models.CharField(verbose_name='User name', max_length=16)
    user_login_datetime = models.DateTimeField(verbose_name='User login datetime')