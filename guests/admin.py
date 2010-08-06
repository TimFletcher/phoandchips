from django.contrib import admin
from models import *

# class GuestPlusXInline(admin.TabularInline):
#     model = GuestPlusX

class GuestAdmin(admin.ModelAdmin):
    # inlines = [GuestPlusXInline]
    pass

admin.site.register(Guest, GuestAdmin)
# admin.site.register(GuestPlusX)