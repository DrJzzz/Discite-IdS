from django.contrib import admin
from notes.models import Note, Tag
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Note, SimpleHistoryAdmin)
admin.site.register(Tag)