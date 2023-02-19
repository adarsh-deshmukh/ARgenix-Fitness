from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render (request,"index.html")
def about_us(request):
    return render (request,"about-us.html")  
def classes(request):
    return render (request,"class-details.html")
def services(request):
    if request.session.has_key("is_logged"):
        return render(request,"services.html")
    else:
        return render(request,"login")

from .forms import membershipForm
from .models import Membership
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def membership(request):
    if request.session.has_key("is_logged"):
        form=membershipForm()
        if request.method=="POST":
            form=membershipForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect ("admission")
            else:
                return redirect("signup")
        return render(request,"membership.html",{"form":form})
    else:
        return render(request,"login.html")

        
def contact(request):
    return render (request,"contact.html")

# Registration

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

def register(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render (request,"register.html",{"form":form})

#Sign up by abstaract user

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import MyUserCreationForm

def signup(request):
    form=MyUserCreationForm()
    if request.method=="POST":
        form=MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render (request,"signup.html",{"form":form})

# login

'''from django.contrib.sessions.models import Session
from django.contrib.auth.models import User,auth

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session["is_logged"]=True
            user1=request.user.username
            request.session["username"]=user1
            response = redirect("admission")
            response.set_cookie("username",username)
            response.set_cookie("login_status",True)
            return response
        else:
            messages.info (request,"Username and Password does not match")
            return redirect ("login")
    return render(request,"login.html")'''

#login with abstract user
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.Admin:
            auth.login(request,user)
            request.session["is_logged"]=True
            user1=request.user.username
            request.session["username"]=user1
            response = redirect("boss")
            response.set_cookie("username",username)
            response.set_cookie("login_status",True)
            return response
        elif user is not None and user.Member:
            auth.login(request,user)
            request.session["is_logged"]=True
            user1=request.user.username
            request.session["username"]=user1
            response = redirect("admission")
            response.set_cookie("username",username)
            response.set_cookie("login_status",True)
            return response
        else:
            messages.info (request,"Username and Password does not match")
            return redirect ("login")
    return render(request,"login.html")



#logout

def logout(request):
    auth.logout(request)
    response=redirect("home")
    return response

#user specific pages

def admission(request):
    return render (request,"admission.html")

from django.views.decorators.csrf import csrf_protect

@csrf_protect
def boss(request):
    return render (request,"boss.html")

# members data which can be seen by boss only
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def showMembers(request):
    if request.session.has_key("is_logged"):
        data=Membership.objects.all()
        return render (request,"showMembers.html",{"data":data})



