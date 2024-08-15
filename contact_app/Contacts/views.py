from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Contacts.forms import RegisterForm,LoginForm,AddContactForm,UpdateContactForm
from Contacts.models import Contacts


# Create your views here.

class HomeView(View):
  def get(self,request):
    if request.user.is_authenticated:
      contacts=Contacts.objects.filter(user=request.user,favorite=True)
      if not(contacts):
        contacts=Contacts.objects.filter(user=request.user).order_by("id")[:15]  
      return render(request, "index.html",{"contacts":contacts})
    else:
      messages.warning(request,"You have to Login!")
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
    messages.success(request,"LogOut !")
    return redirect('login_view')

class AddContactView(View):
  def get(self,request):
    form=AddContactForm()
    return render(request,'add_contact.html',{"form":form})

  def post(self,request):
    if request.user.is_authenticated:
      form=AddContactForm(request.POST)
      if form.is_valid():
        fname=form.cleaned_data.get("first_name")
        lname=form.cleaned_data.get("last_name")
        email=form.cleaned_data.get("e_mail")
        phone=form.cleaned_data.get("phone_no")
        place=form.cleaned_data.get("place")
        Contacts.objects.create(first_name=fname,last_name=lname,e_mail=email,phone_no=phone,place=place,user=request.user)
        messages.success(request,"Contact Added.")
        return redirect("home_view")
      else:
        messages.error(request,"Chack your enterd Data?")
        return redirect("addcontact_view")
    else:
      messages.warning(request,"You have to Login!")
      return redirect('login_view')
    

class ContactListView(View):
  def get(self,request):
    contacts=Contacts.objects.filter(user=request.user)
    return render(request,"list_contacts.html",{"contacts":contacts})


class ContactDetailView(View):
  def get(self,request,*args,**kwargs):
    if request.user.is_authenticated:
      id=kwargs.get('id')
      contact=Contacts.objects.get(id=id)
      print(contact)
      return render(request,"view_contact.html",{"contact":contact})
    else:
      messages.warning(request,"You have to Login!")
      return redirect('login_view')


class UpdateContactView(View):
  def get(self,request,*args,**kwargs):
    if request.user.is_authenticated:
      contact=Contacts.objects.get(id=kwargs.get("id"))
      form=UpdateContactForm(instance=contact)
      return render(request,"update_contact.html",{"form":form})
    else:
      messages.warning(request,"You have to Login!")
      return redirect('login_view')
  def post(self,request,*args,**kwargs):
    contact=Contacts.objects.get(id=kwargs.get("id"))
    form=UpdateContactForm(request.POST,instance=contact)
    if form.is_valid():
      form.save()
      messages.success(request,"Contact Updated.")
      return redirect('listcontact_view')
    else:
      messages.debug(request,"somthing wrong!")
      return redirect('updatecontact_view')


class DeleteContactView(View):
  def get(self,request,*args,**kwargs):
    if request.user.is_authenticated:
      contact=Contacts.objects.get(id=kwargs.get("id"))
      contact.delete()
      messages.success(request,"Contact Deleted!")
      return redirect('listcontact_view')
    else:
      messages.warning(request,"You have to Login!")
      return redirect('login_view')