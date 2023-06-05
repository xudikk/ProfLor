from django.contrib import admin

# Register your models here.
from dashboard.models import Contact, New, Doctor

admin.site.register(Contact)
admin.site.register(New)
admin.site.register(Doctor)