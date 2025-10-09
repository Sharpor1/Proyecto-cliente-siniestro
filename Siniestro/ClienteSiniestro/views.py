from django.shortcuts import render, redirect, get_object_or_404
from .models import Sinis
from .forms import SinisForm
from django.contrib import messages

def sinView(request):
    menu = Sinis.objects.all()
    return render(request, 'ClienteSiniestro/sin_view.html', {'menus': menu})

def sinCreate(request):
    # Crear nuevo siniestro
    form = SinisForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, '¡Siniestro creado con éxito!')
            return redirect('list')  # Asegúrate que 'list' exista en tus urls.py
        else:
            messages.error(request, 'Corrige los errores antes de continuar.')
    return render(request, 'ClienteSiniestro/sin_create.html', {'form': form})

def sinDetail(request, id):
    # Vista de detalle de un siniestro
    siniestro = get_object_or_404(Sinis, id=id)
    return render(request, 'ClienteSiniestro/sin_detail.html', {'siniestro': siniestro})

def sinEvid(request, id):
    # Evidencias o imágenes asociadas al siniestro
    siniestro = get_object_or_404(Sinis, id=id)
    return render(request, 'ClienteSiniestro/sin_evid.html', {'siniestro': siniestro})