from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Students)
admin.site.register(Book_Issue)