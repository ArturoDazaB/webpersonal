from django.contrib import admin
from .models import Description, ExperiencieA, ExperiencieL, skills_idiomas, intereses_aptitudes
# Register your models here.
#============================================================
class DescriptionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Description, DescriptionAdmin)

#============================================================
class ExperiencieAAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','institute')

admin.site.register(ExperiencieA, ExperiencieAAdmin)

#============================================================
class ExperiencieLAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','employeer')

admin.site.register(ExperiencieL, ExperiencieLAdmin)

#============================================================
class skills_idiomasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'category')

admin.site.register(skills_idiomas, skills_idiomasAdmin)

#============================================================
class intereses_aptitudesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'category')  

admin.site.register(intereses_aptitudes, intereses_aptitudesAdmin)