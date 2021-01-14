from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
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
        # Get the post parameters
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

def signin (request):
    if request.method == 'POST':
        #Get the post parameter
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None: 
            messages.success(request, "Sucessfully Login into Kibtrip")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials!  Please try again")
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def log_out(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")   
    return redirect('index')