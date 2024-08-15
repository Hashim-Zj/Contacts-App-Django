from django import forms
from django.contrib.auth.models import User
from Contacts.models import Contacts


class RegisterForm(forms.ModelForm):
  class Meta:
    model=User
    fields=["username","email","password"]
    widgets={
      "username":forms.TextInput(attrs={"class":"form-control my-1","placeholder":"User Name"}),
      "email":forms.EmailInput(attrs={"class":"form-control my-1","placeholder":"Enter email"}),
      "password":forms.PasswordInput(attrs={"class":"form-control my-1","placeholder":"Enter your Password"}),
    }
    help_texts={ "username": None}
    
class LoginForm(forms.ModelForm):
  class Meta:
    model=User
    fields=["username","password"]
    widgets={
      "username":forms.TextInput(attrs={"class":"form-control my-1","placeholder":"UserName"}),
      "password":forms.PasswordInput(attrs={"class":"form-control my-1","placeholder":"Password"}),
    }
    help_texts={ "username": None}

class AddContactForm(forms.ModelForm):
  class Meta:
    model=Contacts
    fields=["first_name","last_name","place","e_mail","phone_no"]
    widgets={
      "first_name":forms.TextInput(attrs={"class":"form-control my-2"}),
      "last_name":forms.TextInput(attrs={"class":"form-control my-2"}),
      "place":forms.TextInput(attrs={"class":"form-control my-2"}),
      "e_mail":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"example@gmail.com"}),
      "phone_no":forms.NumberInput(attrs={"class":"form-control my-2","placeholder":"000 000 0000"}),
    }


class UpdateContactForm(forms.ModelForm):
  class Meta:
    model=Contacts
    fields=["first_name","last_name","place","e_mail","phone_no","favorite"]
    widgets={
      "first_name":forms.TextInput(attrs={"class":"form-control my-2"}),
      "last_name":forms.TextInput(attrs={"class":"form-control my-2"}),
      "place":forms.TextInput(attrs={"class":"form-control my-2"}),
      "e_mail":forms.EmailInput(attrs={"class":"form-control my-2",}),
      "phone_no":forms.NumberInput(attrs={"class":"form-control my-2",}),
      "favorite":forms.CheckboxInput(attrs={"class":"form-check-input",}),
    }