from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

# from . models import Post
from django.http import*
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def index(request):
    return render(request,"index.html")

def register_user(request):

    if request.method=='POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.error(request,"That username has already been used")
                return HttpResponseRedirect("/blog/register_user")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"That email has already been used")
                    return HttpResponseRedirect("/convert/register_user")
        
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                    username=user_name,email=email,password=password)

                    user.save()
                    messages.success(request,"You are now registered and can login")
                    return HttpResponseRedirect("/convert/login_user")
        else:
            messages.error(request,"Passwords do not match")

    return render(request,"register_user.html")


def login_user(request):

    if request.method=="POST":

        user_name = request.POST['user_name']
        password=request.POST["password"]

        user= auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are logged in")
            return HttpResponseRedirect("/convert/dashboard")
        else:
            messages.error(request,"Enter valid username and password")
            return HttpResponseRedirect("/convert/login_user")

    return render(request,"login_user.html")

@login_required
def dashboard(request):
    return render(request,"dashboard.html")

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request,"You are logged out")
        return HttpResponseRedirect("/convert/")