from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from.models import *

# Create your views here.

def main(request):
    gallery_images=Gallery.objects.filter(user=request.user)
    return render(request,'index.html',{"gallery_images":gallery_images})

def login_user(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session["username"]=username
            return redirect(main)
        messages.error(request,"wrong password or username")
        return redirect(login_user)
    return render(request,'login.html')
        
def signup(request):
    if request.POST:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect(login_user)
        messages.error(request,"password doesnot match")
        return redirect(signup)
    return render(request,'signup.html')

def add_user(request):
    if request.method=='POST' and 'image'in request.FILES:
        myimage=request.FILES['image']
        obj=Gallery(feedimage=myimage,user=request.user)
        obj.save()
        return redirect('add_user')
    return render(request,"add.html")

def delete_g(request,id):
    feeds=Gallery.objects.filter(pk=id)
    feeds.delete()  
    return redirect(main)

