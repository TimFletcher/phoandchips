from django.contrib import admin
from models import Entry
from forms import EntryForm

class EntryAdmin(admin.ModelAdmin):

    form = EntryForm

admin.site.register(Entry, EntryAdmin)