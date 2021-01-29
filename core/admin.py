from django.contrib import admin
from core.models import ActivityLog, Localiza, Famoso, Cidade


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class LocalizaAdmin(admin.ModelAdmin):
    list_display = ('famoso', 'cidade', 'data')

class FamosoAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'nome', 'descricao')

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'nome', 'descricao')

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Localiza, LocalizaAdmin)
admin.site.register(Famoso, FamosoAdmin)
admin.site.register(Cidade, CidadeAdmin)