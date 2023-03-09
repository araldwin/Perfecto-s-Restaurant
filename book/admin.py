from django.contrib import admin
from .models import Book


admin.site.site_header = "Perfectos Admin"
admin.site.site_title = "Perfectos Admin Area"
admin.site.index_title = "Welcome to the Perfectos Admin Area"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',
                    'book_date', 'book_time', 'people', 'message',)
    search_fields = ('name', 'phone',
                     'book_date', 'people', 'message')
    list_filter = ('book_date',)
    ordering = ('-book_date',)
