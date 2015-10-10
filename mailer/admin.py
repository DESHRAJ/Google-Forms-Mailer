from django.contrib import admin
from mailer.models import MailTemplate, Person
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Person, PersonAdmin)
admin.site.register(MailTemplate)
