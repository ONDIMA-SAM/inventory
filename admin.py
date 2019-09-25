from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Equipment, StaffRequest


class StaffRequestAdmin(admin.ModelAdmin):
    list_display = ('staff_name', 'staff_department', 'r_equipment')
    list_filter = ['staff_department']

admin.site.register(StaffRequest,StaffRequestAdmin)

def assign_equipment(modeladmin, request, queryset):
    for obj in queryset:
        if obj.assigned_to == 'Not assigned':
            serial = obj.serial_number
            return HttpResponseRedirect(reverse('assign',args=[serial]))

    return HttpResponseRedirect('/inventory')
assign_equipment.short_description = 'Assign selected equipment a user'

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'serial_number', 'status', 'assigned_to', 'department')
    list_filter = ['type']
    actions = [assign_equipment]

admin.site.register(Equipment, EquipmentAdmin)
