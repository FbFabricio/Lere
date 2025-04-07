from django.contrib import admin

from .models import Cliente

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "carro", "placa")
    search_fields = ("nome", "carro", "placa")