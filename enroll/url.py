from django.urls import path
from .import views
urlpatterns = [
    path("",views.home,name='home'),
   # path("",views.home,name='home'),
    path("save/",views.savedata,name='save'),
    path("delete/",views.deletedata,name='delete'),
    path("edit/",views.editdata,name='edit'),
   
]