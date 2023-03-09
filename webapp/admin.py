from django.contrib import admin

from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'text', 'email', 'status', 'created_at', 'updated_ad']
    list_filter = ['author', 'status']
    search_fields = ['author', 'status']
    fields = ['author', 'text', 'email', 'status']
    readonly_fields = ['created_at', 'updated_ad']


admin.site.register(Book, BookAdmin)
