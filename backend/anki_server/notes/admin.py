from django.contrib import admin
from notes.models import Note, Tag
from simple_history.admin import SimpleHistoryAdmin

# class NoteHistoryAdmin(SimpleHistoryAdmin):
#     list_display = 

admin.site.register(Note, SimpleHistoryAdmin)
admin.site.register(Tag)