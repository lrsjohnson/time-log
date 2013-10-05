from django.contrib import admin
from timelog.models import TimeEntry, Tag

admin.site.register(TimeEntry)
admin.site.register(Tag)
