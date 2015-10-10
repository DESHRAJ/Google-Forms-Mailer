from django.db import models
import uuid
# Create your models here.

class MailTemplate(models.Model):
	message = models.TextField(default = None)

class Person(models.Model):
	name = models.CharField(default = None, max_length = 200)

