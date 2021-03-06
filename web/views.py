from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        # Get the post param eters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        # Create New User
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Talent Height account has been successfully created")
        return redirect('index')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        #Get the post parameter
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None: 
            auth_login(request, user)
            messages.success(request, "Sucessfully Login into Kibtrip")
            print("Logged in")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials!  Please try again")
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def logout(request):
    logout(request)
    messages.info(request, "Successfully Logged Out")   
    return redirect('index')

def manage_profile(request):
    return render(request, 'manage-profile.html')

def index_2(request):
    return render(request, 'index-2.html')

def movie_category(request):
    return render(request, 'movie-category.html')

def M_details(request):
    return render(request, 'movie-details.html')

def pricing(request):
    return render(request, 'pricing-plan.html')

def setting(request):
    return render(request, 'setting.html')

def show_category(request):
    return render(request, 'show-category.html')

def S_details(request):
    return render(request, 'show-details.html')

def signle(request):
    return render(request, 'show-signle.html')

def single(request):
    return render(request, 'show-single.html')

def watch(request):
    return render(request, 'watch-video.html')

def showlist(request):
    return render(request, "index.html") 

def contact(request):
    if request.method=="POST":
        try:
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            content =request.POST['content']
            contact=Contact()
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.content = content
            contact.save()
            messages.success(request,'Success')
            return render(request, "contact.html") 
        except Exception as e:
            messages.error(request,'Error: '+str(e))
            print('Error: '+str(e))
            return render(request, "contact.html") 
    else:
        return render(request, "contact.html") 

