from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from .forms import courseForm,createForm  # Make sure this is defined in forms.py
from django.contrib.auth import login,logout,authenticate
from . models import coursedetails,Applymodel
from django import forms
from . forms import RegisterForms
# Create your views here.
def home(request):
    x=coursedetails.objects.all()
    return render(request,'home.html',{'x':x})
def register_views(request):
    if request.method=='POST':
        form=RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegisterForms()
            
    return render(request, 'register.html', {'form': form})

def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_views(request):
    logout(request)
    return redirect('home')


def table(request):
    x=coursedetails.objects.all()
    return render(request,'table.html',{"x":x})

def course(request):
    return render(request,'course.html')


def createcourse(request):
    form=createForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('success')
    
    return render(request,'createcourse.html',{"form": form})


def stdapply(request):
    form = courseForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('success')  # Replace with the name of a success page/view
    
    return render(request, 'stdapply.html', {"form": form})
def success(request):
    return render(request,'success.html')


def delete_course(request, pk):
    course = coursedetails.objects.get(pk=pk)
    course.delete()
    return redirect('home')


def update_course(request, pk):
    course = get_object_or_404(coursedetails, pk=pk)
    if request.method == 'POST':
        form = courseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = courseForm(instance=course)
    return render(request, 'update.html', {'form': form})