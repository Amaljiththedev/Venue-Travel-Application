from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("",views.user_inteface,name="user_interface"),
    path('login',views.user_login,name="user_login"),
    path('register',views.user_register,name="user_register"),
<<<<<<< HEAD
    path('recommandation',views.recommendation,name="recommandation")
=======
>>>>>>> origin/main
]
