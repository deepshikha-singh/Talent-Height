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

def sdetails(request):
    return render(request, 's-details.html')

def signle(request):
    return render(request, 'signle.html')

def single(request):
    return render(request, 'single.html')

def signup(request):
    return render(request, 'sign-up.html')

def watch(request):
    return render(request, 'watch-video.html')

def index2(request):
    return render(request, 'index-2.html')