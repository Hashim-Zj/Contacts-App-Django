from django.urls import path
from Contacts.views import HomeView,LoginView,RegisterView,LogOutView

urlpatterns=[
  path('',HomeView.as_view(),name='home_view'),
  path('login',LoginView.as_view(),name='login_view'),
  path('register',RegisterView.as_view(),name='register_view'),
  path('logout',LogOutView.as_view(),name='logout_view'),
]

