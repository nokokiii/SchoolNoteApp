from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('subjects', views.subjects, name='units')
]
