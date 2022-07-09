from django.urls import path 
from .import views

urlpatterns= [
    path('', views.demohome, name='home'),
    path('newuser/<int:id>', views.newuser, name='newuser'),
    path('about', views.demoaboutus, name='about'),
    path('add', views.addbook, name='add'),
    path('contactus', views.democontact, name='contactus'),
    #path('Register', views.demoRegister, name='Register'),
    path('search', views.demosearch, name='search'),
    path('Student', views.demostudent, name='Student'),
    path('updateuser',views.demoupdateuser, name='updateuser'),
    path('updatespecbook', views.demoupdatespecbook, name='updatespecbook'),
    path('Admin', views.demoadmin, name='Admin'),
    path('list',views.demolist, name='list'),
    path('updatebook',views.demoupdatebook, name='updatebook'),
    path('Register', views.Signup, name= 'Register'), 
    #path('<int: id>' , views.update ,name=update),
    path('AdminContactus', views.democontactadmin, name='AdminContactus'),
    path('StudentContactus', views.democontactstudent, name='StudentContactus'),
    path('listall',views.demolistall, name='listall'),
    path('Borrow', views.borrowabook, name='Borrow'),
    path('return', views.returnabook, name='return'),
    path('<int:ID>', views.update ,name='update'),
   
]