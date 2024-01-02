from django.contrib import admin

from .models import Entry, Topic

# Register your models here.
admin.site.register(Topic) # admin now has access to the Topic database.
admin.site.register(Entry)
