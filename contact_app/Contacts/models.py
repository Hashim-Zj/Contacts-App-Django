from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contacts(models.Model):
  first_name=models.CharField(max_length=50)
  last_name=models.CharField(max_length=50)
  place=models.CharField(max_length=50)
  e_mail=models.CharField(max_length=60, null=False, unique=True)
  phone_no=models.CharField(max_length=15, null=False, unique=True)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  date=models.DateField(auto_now_add=True)
  favorite=models.BooleanField(default=False)

  def __str__(self):
    return self.first_name
  