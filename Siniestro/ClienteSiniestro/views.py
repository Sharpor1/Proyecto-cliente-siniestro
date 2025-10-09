from django.shortcuts import render, redirect, get_object_or_404
from .models import Sinis
from .forms import SinisForm, EvidForm
from django.contrib import messages

def sinView(request):
    return render(request, 'ClienteSiniestro/sin_view.html', {'sinis': Sinis.objects.all})

def sinCreate(request):
    form = SinisForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            siniestro = form.save()  # Guarda y obtiene el objeto creado
            messages.success(request, '¡Siniestro creado con éxito!')
            # Redirige a la vista de evidencias con el id recién creado
            return redirect('evidence', id=siniestro.id)
        else:
            messages.error(request, 'Corrige los errores antes de continuar.')

    return render(request, 'ClienteSiniestro/sin_create.html', {'form': form})

def sinDetail(request, id):
    # Vista de detalle de un siniestro
    siniestro = get_object_or_404(Sinis, id=id)
    return render(request, 'ClienteSiniestro/sin_detail.html', {'siniestro': siniestro})

def sinEvid(request, id):
    print("🟢 ENTRÓ A sinEvid")
    siniestro = get_object_or_404(Sinis, id=id)

    # Carga el formulario SOLO con los campos de evidencia
    form = EvidForm(request.POST or None, request.FILES or None, instance=siniestro)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "¡Evidencias guardadas correctamente!")
            return redirect("list")
        else:
            messages.error(request, "Revisa los campos antes de guardar.")

    context = {
        "form": form,
        "siniestro": siniestro,
    }
    print("➡️ Siniestro:", siniestro.id)
    print("➡️ Campos del form:", form.fields.keys())
    return render(request, "ClienteSiniestro/sin_evid.html", context)