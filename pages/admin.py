# from django.contrib import admin

# # Register your models here.
# from .models import Team

# @admin.register(Team)
# class TeamsAdmin(admin.ModelAdmin):
#     list_display = ('firstname', 'lastname', 'designation', 'created_date')

from django.contrib import admin
from django.utils.html import format_html
from .models import Team

@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        if object.photo:
            return format_html(
                '<img src="{}" width="40" style="border-radius:5px;" />',
                object.photo.url
            )
        return "-"

    thumbnail.short_description = 'Photo'

    list_display = (
        'id',
        'thumbnail',
        'firstname',
        'lastname',
        'designation',
        'created_date',
    )

    list_display_links = ('id', 'thumbnail', 'firstname')

    search_fields = ('firstname', 'lastname', 'designation')

    list_filter = ('designation',)
