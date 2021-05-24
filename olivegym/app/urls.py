from django.urls import path
from.import views
urlpatterns = [
    path('',views.index, name='gymhome'),
    path('about/', views.aboutus, name='about'),
    path('contactus/', views.contactus, name='contact'),
    path('joining/', views.joining, name='join'),
    path('joinsuccess/', views.joinsuccess, name='jsuccess'),
    path('calling/', views.calling, name='call'),
    path('messaging/', views.messaging, name='message'),
    path('fees/', views.fees, name='fees'),


    
       
]