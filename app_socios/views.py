from django.shortcuts import redirect, render

from app_bienes_inmueble.models import Inmuebles
from .models import *

from .forms import *

from django.db.models import Q
from django.db.models import IntegerField
from django.db.models.functions import Cast
# Create your views here.

def socios(request):
    socios = Socios.objects.all()[:15]    
    cantidad_socios = Socios.objects.all().count()
    return render(request,'app_socios/menu_socios.html',{'socios':socios,'cantidad_socios':cantidad_socios})

def filtrar_socios_nombre(request):
    pista_nombre = request.GET.get('nombre','').strip()    
    palabras = pista_nombre.split() # Esto crea ['Samir', 'Quispe']
    query = Q()
    for palabra in palabras:
        # Por cada palabra, buscamos en nombres O apellidos
        query &= (Q(nombres__icontains=palabra) | Q(apellidos__icontains=palabra))

    socios = Socios.objects.filter(query)    
    return render(request,'app_socios/socios_filtrados.html',{'socios':socios})
    

def ver_detalles_socio(request,pk):
    socio = Socios.objects.get(pk=pk)
    huertos_socio = Inmuebles.objects.filter(tipo=1,socio_relacionado=socio)
    parcelas_socio = Inmuebles.objects.filter(tipo=2,socio_relacionado=socio)
    codigos_asociados = CodigosAsociadosSocio.objects.filter(
        socio_asociado=pk
    ).annotate(
        codigo_int=Cast('codigo', output_field=IntegerField())
    ).order_by('codigo_int')
    personas_asociadas = PersonasRelacionadasSocio.objects.filter(socio_asociado=pk)
    return render (request,'app_socios/ver_detalles_socio.html',{'socio':socio,'huertos_socio':huertos_socio,'parcelas_socio':parcelas_socio,'codigos_asociados':codigos_asociados,'personas_asociadas':personas_asociadas})
    

def editar_socio(request,pk):
    socio = Socios.objects.get(pk=pk)
    huertos_socio = Inmuebles.objects.filter(tipo=1,socio_relacionado=socio)
    parcelas_socio = Inmuebles.objects.filter(tipo=2,socio_relacionado=socio)
    codigos_asociados = CodigosAsociadosSocio.objects.filter(
        socio_asociado=pk
    ).annotate(
        codigo_int=Cast('codigo', output_field=IntegerField())
    ).order_by('codigo_int')
    personas_asociadas = PersonasRelacionadasSocio.objects.filter(socio_asociado=pk)
    if request.method == 'POST':
        form = SocioFormulario(request.POST,instance=socio)
        if form.is_valid():
            form.save()
            return redirect('ver_detalles_socio',pk=socio.id)
    else:
        form = SocioFormulario(instance=socio)
    return render(request,'app_socios/editar_socio.html',{'form':form,'huertos_socio':huertos_socio,'parcelas_socio':parcelas_socio,'codigos_asociados':codigos_asociados,'personas_asociadas':personas_asociadas})

def buscar_socio(request):
    return render(request,'app_socios/buscar_socio.html')

def encontrar_socios(request):
    pista_socio = request.GET.get('socio')
    palabras = pista_socio.split()
    query = Q()
    for palabra in palabras:
        query &= (Q(nombres__icontains=palabra) | Q(apellidos__icontains=palabra))
    socios = Socios.objects.filter(query)
    return render(request,'app_socios/socios_encontrados.html',{'socios':socios})  