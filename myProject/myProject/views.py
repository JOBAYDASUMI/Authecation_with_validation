from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from myApp.models import *
from django.contrib import messages

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError
from django.http import Http404

from django.db.models import Q 


def homePage(req):
    return render(req,'common/home.html')

def loginPage(req):
    if req.method=='POST':
        User_name=req.POST.get('name')
        Password=req.POST.get('psw')


        if not User_name or not Password:
            messages.warning(req, "Both username and password are required")
            return render(req, "loginPage.html")

        user = authenticate(username=User_name, password=Password)

        if user is not None:
            login(req, user)
            messages.success(req, "Login Successfully")
            return redirect("jobFeddPage")
        else:
            messages.warning(req, "Invalid username or password")
    return render(req,"common/loginpage.html")

def logoutPage(req):
    logout(req)
    return redirect('loginPage')



def registrationPage(req):
    if req.method=='POST':
        User_name=req.POST.get('name')
        Email=req.POST.get('email')
        User_type=req.POST.get('user_type')
        Password=req.POST.get('psw')
        Confirm_password=req.POST.get('Cpsw')

        if not all([User_name,Email,User_type,Password,Confirm_password]):
            messages.warning(req, "All Field Are Requered")
            return render(req, "common/registerPage.html")
        try: 
            validate_email(Email)
        except ValidationError:
            messages.warning(req,"Invalid Email Firmate")
            return render(req, "common/registerPage.html")
        if Password != Confirm_password:
            messages.warning(req,"Password Not Meatched")
            return render(req,"common/registerPage.html")
        if len(Password) < 8:
            messages.warning(req,"Password must be at least 8 characters long")
            return render(req,"common/registerPage.html")
        
        if not any(char.isdigit() for char in Password) or not any(char.isalpha() for char in Password):
            messages.warning(req,"Password must contain both letters and numbers")
            return render(req, "common/registerPage.html")


        
        try:
            user = custom_user.objects.create_user(
                username=User_name,
                email=Email,
                user_type=User_type,
                password=Password,
            )
            messages.success(req,"Account created successfully! Please log in.")
            return redirect("loginPage")
        except IntegrityError:
           messages.warning(req, "Username or email already exists")
           return render(req, "common/registerPage.html")

    return render(req,"common/registerPage.html")


def logoutPage(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("loginPage")


def jobFeddPage(req):

    return render(req,"common/jobFeddPage.html")









