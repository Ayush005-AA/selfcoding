
from django.urls import path
from mainpge import views

urlpatterns = [
    path("",views.homefun,name="home")
    
]
