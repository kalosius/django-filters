from django.contrib import admin
from . models import *
# Register your models here
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name',]

class BookAdmin(admin.ModelAdmin):
    list_display=['name',]
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
