from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    #template=loader.get_template('authentication\index.html')
    return render(request,'authentication/index.html')

def signup(request):
    if request.method=="POST":
       username=request.POST["username"]
       fname=request.POST["fname"]
       lname=request.POST["lname"]
       email=request.POST["email"]
       pass1=request.POST["pass1"]
       pass2=request.POST["pass2"]       

       myuser=User.objects.create_user(username,email,pass1)
       myuser.first_name="fname"
       myuser.last_name="lname"

       myuser.save()

       messages.success(request,"You have successfully logged in")
       return redirect('/signin')


    return render(request,'authentication\signup.html')


def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["pass1"]

        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return redirect('/dashboard')
            return render(request,'authentication/index.html',{'fname':fname})

        else:
            messages.error(request,"Bad Credentials")
        
    return render(request,'authentication/signin.html')

#@login_required
def dashboard(request):
   return render(request,'authentication/dashboard.html')

def videocall(request):
    return render(request,'authentication/videocon.html')

def signout(request):
   logout(request)
   messages.success(request,"Logged out Successfully")
   return redirect('home')

def join(request):
    if request.method == 'POST':
        roomid = request.POST['roomid']
        return redirect("/meeting?roomid="+roomid)
    return render(request,'authentication/join.html')