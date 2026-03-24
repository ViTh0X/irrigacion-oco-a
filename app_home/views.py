from django.shortcuts import render

# Create your views here.


def home_irrigacion_ocoña(request):
    return render(request,'app_home/irrigacion_ocoña.html')