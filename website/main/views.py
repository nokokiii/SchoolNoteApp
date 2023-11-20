from django.shortcuts import render

# Create your views here.
def subjects(request):
    return render(request, 'subjects.html')
