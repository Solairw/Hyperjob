# from django.db import models
# import django.contrib.auth.models
# from django.utils import timezone
#
# # Create your models here.
#
# user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#
#
# class Resume(models.Model):
#     description = models.CharField(max_length=1024)
#     author = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    description = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
