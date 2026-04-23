from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'Registration successful ,You login')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed')
    else:
        form = RegistrationForm()
    return render(request, 'user_auth/register.html', {'form':form})

def user_login(request):
    if request.method =='POST':
         form = AuthenticationForm(request , data = request.POST)
         if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username =username, password = password)
           if user is not None:
              login(request, user) 
              return redirect('dashboard')
           else:
              messages.error(request,'login failed')
         else:
               messages.error(request, 'Invalid login details')   
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html',{'form':form})     

def user_logout(request):
    logout(request)
    messages.success(request,'logout successful') 
    return redirect('user_login')  
def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "Login First!")
        return redirect('user_login')
    
    return render(request, 'user_auth/dashboard.html', {'user': request.user})
     