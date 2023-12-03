from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('units', views.units, name='units'),
    path('unit/<int:unitId>', views.unit, name='unit'),
    path('units/delete/<int:unitId>', views.delete_unit, name='delete_unit'),
    path('units/add', views.add_unit, name='add_unit'),
    path('notes/add/<int:unitId>', views.add_note, name='add_note'),
    path('notes/delete/<int:noteId>', views.delete_note, name='delete_note'),
    path('notes/edit/<int:noteId>', views.edit_note, name='edit_note')
]
