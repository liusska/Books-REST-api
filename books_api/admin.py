from django.contrib import admin

from books_api.models import BookModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    pass
