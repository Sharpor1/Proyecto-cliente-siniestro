from django.contrib import admin
from .models import Sinis

@admin.register(Sinis)
class SinisAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'fecha', 'estado')
    search_fields = ('asunto', 'descripcion', 'estado')
    list_filter = ('estado', 'fecha')