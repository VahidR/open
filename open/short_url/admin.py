from django.contrib import admin

from .models import Link

class LinkAdmin(admin.ModelAdmin):
	fields = ('url',)
	list_display = ('url', 'hash_code')

admin.site.register(Link, LinkAdmin)
