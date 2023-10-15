from django.urls import path
from . import views

urlpatterns=[
    path('',views.main,name='main'),
    path('members/',views.member,name='member'),
    path('members/details/<slug:slug>',views.details,name='details'),
     path('testing/', views.testing, name='testing'),
    
]