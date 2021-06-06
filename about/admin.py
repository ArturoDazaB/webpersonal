from django.contrib import admin
from .models import Description, ExperiencieA, ExperiencieL

# Register your models here.
#============================================================
class DescriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Description, DescriptionAdmin)

#============================================================
class ExperiencieAAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ExperiencieA, ExperiencieAAdmin)

#============================================================
class ExperiencieLAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ExperiencieL, ExperiencieLAdmin)