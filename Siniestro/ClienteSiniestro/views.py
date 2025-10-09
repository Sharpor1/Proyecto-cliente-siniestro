from django.shortcuts import render, redirect, get_object_or_404
from .models import Sinis
from .forms import SinisForm, EvidForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def sinView(request):
    return render(request, 'ClienteSiniestro/sin_view.html', {'sinis': Sinis.objects.all})


def sinCreate(request):
    form = SinisForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST":
        if form.is_valid():
            siniestro = form.save() 
            messages.success(request, '¡Siniestro creado con éxito!')

            return redirect('evidence', id=siniestro.id)
        else:
            messages.error(request, 'Corrige los errores antes de continuar.')

    return render(request, 'ClienteSiniestro/sin_create.html', {'form': form})


def sinDetail(request, id):
    # Vista de detalle de un siniestro
    siniestro = get_object_or_404(Sinis, id=id)
    return render(request, 'ClienteSiniestro/sin_detail.html', {'siniestro': siniestro})

def sinEvid(request, id):
    siniestro = get_object_or_404(Sinis, id=id)
    form = EvidForm(request.POST or None, request.FILES or None, instance=siniestro)

    if request.method == "POST":
        if form.is_valid():
            sin_obj = form.save(commit=False)

            for i in range(1, 6):
                imagen_campo = f"imagen{i}"
                expli_campo = f"expli{i}"

                nueva_img = request.FILES.get(imagen_campo)
                nueva_expli = request.POST.get(expli_campo)

                if not nueva_img:
                    # Mantiene la imagen anterior
                    setattr(sin_obj, imagen_campo, getattr(siniestro, imagen_campo))
                else:

                    if not nueva_expli and getattr(siniestro, expli_campo):
                        setattr(sin_obj, expli_campo, getattr(siniestro, expli_campo))

            sin_obj.save()
            messages.success(request, "✅ ¡Evidencias agregadas correctamente!")
            return redirect("detail", id=siniestro.id)
        else:
            messages.error(request, "⚠️ Revisa los campos antes de guardar.")

    context = {
        "form": form,
        "siniestro": siniestro,
    }
    return render(request, "ClienteSiniestro/sin_evid.html", context)