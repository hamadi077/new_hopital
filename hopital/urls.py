
from django.urls import path
from hopital.views import *

urlpatterns = [
    path('',home, name='homepage'),
    path('about/',about , name='about'),
    path('createaccount/',createaccountpage , name='createaccountpage'),
    path('login/',loginpage , name='loginpage'),
    path('logout/',logoutt , name='logout'),
    path('profile/',patientprofile , name='profile'),
    path('rendezvous/',make_apointement , name='rendezvous'),
    path('admin_home/',AdminHome , name='admin_home'),
    path('addDoctor/',add_doctor , name='addDoctor'),
    path('viewmedecin/',adminviewDoctor , name='viewmedecin'),
    path('profiled/',doctorprofile , name='profiled'),
]
