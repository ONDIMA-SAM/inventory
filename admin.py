from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Equipment

#admin.site.register(Equipment)

def assign_equipment(modeladmin, request, queryset):
    #queryset.update(assigned_to='sam')
    for obj in queryset:
        if obj.assigned_to != 'Not assigned':
            return HttpResponseRedirect('/inventory/assign')

    return HttpResponseRedirect('/inventory/assign')
assign_equipment.short_description = 'Assign selected equipment a user'

class EquipmentAdmin(admin.ModelAdmin):
    #fields = ['type', 'vendor', 'status']
    list_display = ('id', 'type', 'vendor', 'status', 'assigned_to', 'department')
    list_filter = ['type']
    actions = [assign_equipment]

admin.site.register(Equipment, EquipmentAdmin)
