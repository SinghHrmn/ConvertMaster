from django.contrib.auth.decorators import *
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse
import os
from django.http import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.conf import settings



# Create your views here.

# ===============================================================================================
def index(request):
    return render(request, 'index.html')

# ====================================Register User==============================================

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
                return HttpResponseRedirect(reverse('register'))
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"That email has already been used")
                    return HttpResponseRedirect(reverse('register'))
        
                else:
                    # Saving the User in the Database
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                    username=user_name,email=email,password=password)
                    user.save()

                    # Making Specified Directory for every User 
                    os.mkdir(os.path.join(settings.MEDIA_ROOT, user_name))
                    
                    messages.success(request,"You are now registered and can login")
                    return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request,"Passwords do not match")

    return render(request,"accounts/register_user.html")

# ======================================Login User===============================================

def login_user(request):

    if request.method=="POST":

        user_name = request.POST['user_name']
        password=request.POST["password"]

        user= auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['User'] = user_name
            messages.success(request,"You are logged in")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request,"Enter valid username or password")
            return HttpResponseRedirect(reverse('login'))

    return render(request,"accounts/login_user.html")

# ======================================Logout==================================================
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        # messages.success(request,"You are logged out")
        return HttpResponseRedirect(reverse('index'))