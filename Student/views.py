from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from.models import Contact, Student_create

from .forms import StudentForm
# Create your views here.


def contact_form(request):
    return render (request,'contact.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            Contact.objects.create(name =name, message = message)
            return HttpResponse(f"thank you {name} for your message")
        else:
            return HttpResponse("please enter the both name and message")
    return redirect( request,'contact_form')


def student_create(request):
    if request.method =='POST':
        # user ne jo data fill kiya hai wo student form me dedo
        form = StudentForm(request.POST)
        # check karo ki data are validate
        if form.is_valid():
            form.save()
            return render(request,'student_success.html')
    else:
        form = StudentForm()    
    return render(request,'student_form.html',{'form':form })    

def student_list(request):
    students = Student_create.objects.all()
    return render(request, 'student_list.html',{'students':students})   

def student_edit(request ,pk):
    student = get_object_or_404(Student_create, pk=pk)
    if request.method =='POST':
        form = StudentForm(request.POST, instance= student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request,'student_form.html',{'form':form})        

def student_delete(request,pk):
    student = get_object_or_404(Student_create,pk = pk)
    if request.method =='POST':
        student.delete()
        return redirect('student_list')
    return render(request,'student_confirm_delete.html',{'student':student})
        
    
    