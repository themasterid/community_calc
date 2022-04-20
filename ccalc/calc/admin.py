from django.contrib import admin

from .models import Bb


class BbAdmin(admin.ModelAdmin):
    list_display = ('ammount', 'comment', 'published')
    list_display_links = ('ammount',)
    search_fields = ('ammount', 'comment', 'published')
    list_editable = ('comment',)


admin.site.register(Bb, BbAdmin)
