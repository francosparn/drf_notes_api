from django.contrib import admin
from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['content', 'created_at', 'user']
    list_filter = ['user']
    list_per_page = 10