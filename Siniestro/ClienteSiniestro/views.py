# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sinis
from .forms import SinisForm
from django.contrib import messages

# Create your views here.

def sinView(request):
    return render(request, 'ClienteSiniestro/sin_view.html', {'sinis': Sinis.objects.all})

def sinCreate(request):
    form = SinisForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Siniestro Creado!')
            return redirect('list')
    return render(request, 'ClienteSiniestro/sin_create.html', {'form': form})

def sinDetail(request):
    return render(request, 'ClienteSiniestro/sin_detail.html')


def sinEvid(request):
    return render(request, 'ClienteSiniestro/sin_evid.html')