from django.urls import path
from authuser import views

urlpatterns = [
     path('about/',views.about,name='about'),
    
     path('contact/',views.contact,name='contact'),
     path('login/',views.login_user,name='login'),
     path('candidte-register/',views.candidateregister,name='register'),
     path('register/',views.register,name='register-user'),
     path('hr-register/',views.hrregister,name='register-hr'),
     path('logout/',views.logoutUser,name='logout'),
     path('contact-submit/', views.contact_submit, name='contact-submit'),
     path('', views.home, name='home'),
    
]
