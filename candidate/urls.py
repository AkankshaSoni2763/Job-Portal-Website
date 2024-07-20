from django.urls import path
from candidate import views
urlpatterns = [
     path('',views.caHome, name='dash'),
     path('dash/',views.caHome, name='dash'),

     path('mylist/',views.myJob,name='mylist'),
     path('applyjob/<int:id>/',views.applyJob,name='applyjob'),
]
