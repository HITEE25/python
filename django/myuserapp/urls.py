from .import views
from django.urls import path

urlpatterns = [
    path('',views.mainpage),
    path('home',views.homepage),
    path('about',views.aboutpage)
]