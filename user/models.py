from django.db import models

# Create your models here.

class User(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=50)
	email = models.EmailField(null=True, blank=True)
	post = models.IntegerField(default=0)
