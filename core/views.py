from django.shortcuts import render

def home(request):
    return render(request, 'core/templates/home.html')
