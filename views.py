from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import EquipmentEntryForm, AssignmentForm
from .models import Equipment

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EquipmentEntryForm(request.POST)
        if form.is_valid():
            print("hello there")
            form.save()

    else:
        form = EquipmentEntryForm()

    context = {'form': form}

    return render(request,'equip_entry.html', context)

def assign(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        #if form.is_valid():
        if form.is_valid():
            form.save()
    form = AssignmentForm()
    context = {'form': form}

    return render(request,'equipment_assignment.html', context)
