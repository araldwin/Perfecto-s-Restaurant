from django.contrib import admin
from .models import Branch
from .models import MyRestaurantUser
from .models import Book


admin.site.site_header = "Perfectos Admin"
admin.site.site_title = "Perfectos Admin Area"
admin.site.index_title = "Welcome to the Perfectos Admin Area"

admin.site.register(MyRestaurantUser)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'branch',
                    'book_date', 'people', 'message', 'myrestaurantuser',)
    search_fields = ('name', 'phone', 'branch',
                    'book_date', 'people', 'message')
    list_filter = ('book_date', 'branch')
    ordering = ('-book_date',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_phone',
                    'branch_email', 'address')
    ordering = ('name',)
    search_fields = ('name',)
