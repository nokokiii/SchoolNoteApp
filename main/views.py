from django.shortcuts import render, redirect

# Create your views here.
def subjects(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    return render(request, 'subjects.html')
    