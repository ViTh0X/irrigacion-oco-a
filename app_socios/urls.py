from django.urls import path
from . import views

urlpatterns = [
    path('',views.socios,name='socios'),
    path('filtrar-socios',views.filtrar_socios_nombre,name='filtrar_socios_nombre'),
    path('detalles-socios/<int:pk>',views.ver_detalles_socio,name='ver_detalles_socio'),
    path('editar-socio/<int:pk>',views.editar_socio,name='editar_socio'),
    path('buscar-socio',views.buscar_socio,name='buscar_socio'),
    path('encontrar-socios',views.encontrar_socios,name='encontrar_socios'),
]
