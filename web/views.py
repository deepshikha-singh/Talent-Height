from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show(request):
    return render(request, 'show-category.html')

def movie(request):
    return render(request, 'movie-category.html')

def manage(request):
    return render(request, 'manage-profile.html')

def details(request):
    return render(request, 'movie-details.html')

def pricing(request):
    return render(request, 'pricing-plan.html')

def reset(request):
    return render(request, 'reset-password.html')

def setting(request):
    return render(request, 'setting.html')

def login(request):
    return render(request, 'login.html')