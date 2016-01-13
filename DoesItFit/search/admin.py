from django.contrib import admin

# Register your models here.
from .models import Article, VendorWebsite

admin.site.register(Article)
admin.site.register(VendorWebsite)