from django.db import models
import uuid
# Create your models here.

class MailTemplate(models.Model):
	message = models.TextField(default = None)

class Person(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(default = None)

