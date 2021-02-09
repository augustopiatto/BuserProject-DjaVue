from django.contrib import admin
from core.models import ActivityLog, Localiza, Famoso, Cidade, Profile


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class LocalizaAdmin(admin.ModelAdmin):
    list_display = ('famoso', 'cidade', 'data', 'id')

class FamosoAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'nome', 'descricao', 'id')

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('imagem', 'nome', 'descricao', 'id')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'user_id')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Localiza, LocalizaAdmin)
admin.site.register(Famoso, FamosoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Profile, ProfileAdmin)
