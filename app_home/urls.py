from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_irrigacion_ocoña,name='home_irrigacion_ocoña'),
]