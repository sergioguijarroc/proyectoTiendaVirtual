from django.contrib import admin
from .models import User, Producto, Marca, Compra
from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Compra)
