from django.contrib import admin
from .models import Project, ProjectImages

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)

class ProjectImagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'project', 'default')

admin.site.register(ProjectImages, ProjectImagesAdmin)
