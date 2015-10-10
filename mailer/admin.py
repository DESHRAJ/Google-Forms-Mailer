from django.contrib import admin
from mailer.models import MailTemplate, Person
# Register your models here.
admin.site.register(MailTemplate)
admin.site.register(Person)
