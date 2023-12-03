from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Units, Notes
from .forms import UnitForm, NoteForm

# Create your views here.
def units(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    units = Units.objects.all()
    return render(request, 'units.html', {'units': units})


def add_unit(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('history:units')
    else:
        form = UnitForm()
    return render(request, 'unit_add.html', {'form': form})

def delete_unit(request, unitId):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    unit = Units.objects.get(pk=unitId)
    unit.delete()
    return redirect('/history/units')


def unit(request, unitId):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    unit = Units.objects.get(pk=unitId)
    notes = Notes.objects.all().filter(unitId=unitId)
    return render(request, 'unit.html', {'unit': unit, 'notes': notes})


def add_note(request, unitId):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    unit = Units.objects.get(pk=unitId)
    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.unitId = unit
            note.save()
            return redirect(f'/history/unit/{unitId}')
    else:
        form = NoteForm()
    return render(request, 'note_add.html', {'form': form})


def delete_note(request, noteId):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    note = Notes.objects.get(pk=noteId)
    note.delete()
    return redirect(f'/history/unit/{note.unitId.unitId}')


def edit_note(request, noteId):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    note = Notes.objects.get(pk=noteId)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(f'/history/unit/{note.unitId.unitId}')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edit.html', {'form': form})
