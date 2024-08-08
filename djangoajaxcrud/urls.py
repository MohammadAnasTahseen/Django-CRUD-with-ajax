    
from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('enroll.url')),
    path("user/",include('enroll.url')),
    
    
]
