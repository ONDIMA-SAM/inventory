from django.forms import ModelForm
from .models import Equipment

class EquipmentEntryForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['type', 'mac_address', 'serial_number','vendor','status']
    #type = forms.CharField(label='Type', max_length=15)
    #mac = forms.CharField(label='Mac address', max_length=20)
    #serial = forms.CharField(label='Serial number', max_length=20)
    #status = forms.CharField(label='Status', max_length=10)
    #author = forms.CharField(label='Entered by', max_length=20)


class AssignmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['assigned_to', 'department', 'id']
