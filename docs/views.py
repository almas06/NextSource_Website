from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginuser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Subject

# Create your views here.
def index(request):
    subjects = Subject.objects.all()
    user = request.user
    return render(request,'index.html',context={'user' : user, 'subjects':subjects})


def loginUser(request): 
    if request.method == 'GET':
        return render(request , 'loginUser.html') 
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginuser(request , user)
                return redirect('index')
        else:
            return render(request , 'login.html')  


def signup(request):
    if request.method == "POST":
        username  = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists() or  User.objects.filter(email=email).exists():
            return render(request,'signup.html')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return render(request,'loginUser.html')
            
    else:
        return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect('index')  

def dsa(request):
    return render(request,'dsa.html')
