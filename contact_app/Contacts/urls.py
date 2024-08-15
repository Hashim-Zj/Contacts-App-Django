from django.urls import path
from Contacts import views

urlpatterns=[
  path('',views.HomeView.as_view(),name='home_view'),
  path('login',views.LoginView.as_view(),name='login_view'),
  path('register',views.RegisterView.as_view(),name='register_view'),
  path('logout',views.LogOutView.as_view(),name='logout_view'),
  path('addcontact',views.AddContactView.as_view(),name='addcontact_view'),
  path('listcontact',views.ContactListView.as_view(),name='listcontact_view'),
  path('detailcontact/<int:id>/', views.ContactDetailView.as_view(),name='detailcontact_view'),
  path('updatecontact/<int:id>/', views.UpdateContactView.as_view(),name='updatecontact_view'),
  path('deletecontact/<int:id>/', views.DeleteContactView.as_view(),name='deletecontact_view'),
]

