from django.contrib import admin
from flatblocks.models import FlatBlock
from flatblocks.forms import FlatBlockAdminForm

class FlatBlockAdmin(admin.ModelAdmin):
    form = FlatBlockAdminForm

    ordering = ['slug', ]
    list_display = ('slug', 'header')
    search_fields = ('slug', 'header', 'content')

admin.site.register(FlatBlock, FlatBlockAdmin)
