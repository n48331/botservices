from django.contrib import admin
from .models import Project, Communication, File
# Register your models here.
admin.site.register(Project)
admin.site.register(Communication)
admin.site.register(File)