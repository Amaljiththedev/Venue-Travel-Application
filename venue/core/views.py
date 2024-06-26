from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"core/index.html")

def login(request):
    return render(request,"registration/login.html")

def registeration(request):
    return render(request,"registration/register.html")