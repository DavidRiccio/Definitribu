from django.contrib import admin

from .models import Wave

# Register your models here.


class WavesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Wave, WavesAdmin)
