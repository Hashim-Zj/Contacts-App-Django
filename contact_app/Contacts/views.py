from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Contacts.forms import RegisterForm,LoginForm,ContactForm


# Create your views here.

class HomeView(View):
  def get(self,request):
    if request.user.is_authenticated:
      return render(request, "index.html")
    else:
      return redirect('login_view')

  
class RegisterView(View):
  def get(self,request):
    form=RegisterForm()
    return render(request,'register.html',{"form":form})

  def post(self,request):
    form=RegisterForm(request.POST)
    if form.is_valid():
      uname=form.cleaned_data.get("username")
      email=form.cleaned_data.get("email")
      psw=form.cleaned_data.get("password")
      User.objects.create_user(username=uname,email=email,password=psw)
      messages.success(request,"User Register Successfull!")
      return redirect('login_view')
    else:
      messages.error(request,"Invalid credentials!")
      return redirect('register_view')


class LoginView(View):
  def get(self,request):
    form=LoginForm()
    return render(request,"login.html",{"form":form})
  
  def post(self,request):
    uname=request.POST.get("username")
    psw=request.POST.get("password")
    user=authenticate(request,username=uname,password=psw)
    if user:
      login(request,user)
      messages.success(request,"Login Successfull!")
      return redirect('home_view')
    else:
      messages.error(request,"Invaleid Credentials!")
      return redirect('login_view')

class LogOutView(View):
  def get(self,request):
    logout(request)
    messages.success(request,"LogOut Successful!")
    return redirect('login_view')