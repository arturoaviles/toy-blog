from django.contrib import admin
from .models import Article, Writer
# Register your models here.

admin.site.register(Writer)
admin.site.register(Article)
