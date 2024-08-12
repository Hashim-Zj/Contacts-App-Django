from django import forms
from django.contrib.auth.models import User
from Contacts.models import Contacts


class RegisterForm(forms.ModelForm):
  class Meta:
    model=User
    fields=["username","email","password"]
    widgets={
      "username":forms.TextInput(attrs={"class":"form-control","placeholder":"User Name"}),
      "email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter email"}),
      "password":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Password"}),
    }
    help_texts={ "username": None}
    
class LoginForm(forms.ModelForm):
  class Meta:
    model=User
    fields=["username","password"]
    widgets={
      "username":forms.TextInput(attrs={"class":"form-control","placeholder":"UserName"}),
      "password":forms.TextInput(attrs={"class":"form-control","placeholder":"Password"}),
    }
    help_texts={ "username": None}

class ContactForm(forms.ModelForm):
  class Meta:
    model=Contacts
    fields=["first_name","last_name","place","e_mail","phone_no"]
    widgets={
      "first_name":forms.TextInput(attrs={"class":"form-control"}),
      "last_name":forms.TextInput(attrs={"class":"form-control"}),
      "place":forms.TextInput(attrs={"class":"form-control"}),
      "e_mail":forms.EmailInput(attrs={"class":"form-control"}),
      "phone_no":forms.NumberInput(attrs={"class":"form-control"}),
    }