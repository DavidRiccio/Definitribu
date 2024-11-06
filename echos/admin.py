from django.contrib import admin

from .models import Echo

# Register your models here.


class EchosAdmin(admin.ModelAdmin):
    pass


admin.site.register(Echo, EchosAdmin)
