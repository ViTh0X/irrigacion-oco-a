from django.shortcuts import redirect, render
from django.http import Http404
from .models import *

from .forms import *

# Create your views here.

def menu_bienes_inmueble_huertos(request):
    #tipo_huerto = TipoInmueble.objects.get(pk=1)    
    huertos = Inmuebles.objects.filter(tipo=1)[:15]
    cantidad_huertos = Inmuebles.objects.filter(tipo=1).count()
    personas_relacionadas_huerto = PersonasRelacionadasSocio.objects.all()
    return render(request,'app_bienes_inmueble/menu_bienes_huertos.html',{'huertos':huertos,'personas_relacionadas_huerto':personas_relacionadas_huerto,'cantidad_huertos':cantidad_huertos})    


def filtrar_huertos_nombres(request):
    pista_huerto = request.GET.get('huerto','').strip()
    #tipo_huerto = TipoInmueble.objects.get(pk=1)    
    huertos = Inmuebles.objects.filter(tipo=1)
    huertos = huertos.filter(nombre__icontains=pista_huerto)
    personas_relacionadas_huerto = PersonasRelacionadasSocio.objects.all()
    return render(request,'app_bienes_inmueble/menu_bienes_huertos_filtrado.html',{'huertos':huertos,'personas_relacionadas_huerto':personas_relacionadas_huerto})

def detalles_huertos(request,pk):
    huerto = Inmuebles.objects.get(pk=pk)
    personas_relacionadas = PersonasRelacionadasSocio.objects.filter(socio_asociado=huerto.socio_relacionado)        
    return render(request,'app_bienes_inmueble/ver_detalles_huertos.html',{'huerto':huerto,'personas_relacionadas':personas_relacionadas})
    
def editar_huerto(request,pk):
    huerto = Inmuebles.objects.get(pk=pk)
    personas_relacionadas = PersonasRelacionadasSocio.objects.filter(socio_asociado=huerto.socio_relacionado)        
    if request.method == 'POST':
        form = HuertoFormulario(request.POST, instance=huerto)
        if form.is_valid():
            form.save()
            return redirect('detalles_huertos',pk=huerto.id)
    else:
        form = HuertoFormulario(instance=huerto)
    return render(request,'app_bienes_inmueble/editar_huerto.html',{'form':form,'huerto':huerto,'personas_relacionadas':personas_relacionadas})
        

def menu_bienes_inmueble_parcelas(request):
    #tipo_huerto = TipoInmueble.objects.get(pk=1)    
    parcelas = Inmuebles.objects.filter(tipo=2)[:15]
    cantidad_parcelas = Inmuebles.objects.filter(tipo=2).count()
    personas_relacionadas_huerto = PersonasRelacionadasSocio.objects.all()
    return render(request,'app_bienes_inmueble/menu_bienes_parcelas.html',{'parcelas':parcelas,'personas_relacionadas_huerto':personas_relacionadas_huerto,'cantidad_parcelas':cantidad_parcelas})    


def filtrar_parcelas_nombres(request):
    pista_parcela = request.GET.get('parcela','').strip()
    #tipo_huerto = TipoInmueble.objects.get(pk=1)    
    parcelas = Inmuebles.objects.filter(tipo=2)
    parcelas = parcelas.filter(nombre__icontains=pista_parcela)    
    return render(request,'app_bienes_inmueble/menu_bienes_parcelas_filtrado.html',{'parcelas':parcelas})

def detalles_parcelas(request,pk):
    parcela = Inmuebles.objects.get(pk=pk)
    personas_relacionadas = PersonasRelacionadasSocio.objects.filter(socio_asociado=parcela.socio_relacionado)        
    return render(request,'app_bienes_inmueble/ver_detalles_parcelas.html',{'parcela':parcela,'personas_relacionadas':personas_relacionadas})
    
def editar_parcela(request,pk):
    parcela = Inmuebles.objects.get(pk=pk)
    personas_relacionadas = PersonasRelacionadasSocio.objects.filter(socio_asociado=parcela.socio_relacionado)        
    if request.method == 'POST':
        form = HuertoFormulario(request.POST, instance=parcela)
        if form.is_valid():
            form.save()
            return redirect('detalles_parcelas',pk=parcela.id)
    else:
        form = HuertoFormulario(instance=parcela)
    return render(request,'app_bienes_inmueble/editar_parcela.html',{'form':form,'parcela':parcela,'personas_relacionadas':personas_relacionadas})
    