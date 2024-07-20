from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
# from homepage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('authuser.urls')),
    path('candidate/',include('candidate.urls')),
     
    path('hr/',include('hr.urls')),
    # path('homepage/', home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 