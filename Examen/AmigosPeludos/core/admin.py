from unicodedata import category
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Categoria, Producto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Permission)
admin.site.register(ContentType)