from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages


# Create your views here.

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture upload')
            return redirect('view_profile')
        else:
            messages.error(request, 'error uploading profile picture')
    else:
        form = ProfileForm()
    return render(request, 'md_files/upload_profile.html', {'form':form})


def view_profile(request):
    profiles = Profile.objects.all()
    
    return render(request ,'md_files/view_profile.html', {'profiles':profiles})            