# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from .forms import MenuForm
from django.contrib import messages

# Create your views here.
def sinView(request):
    return render(request, 'ClienteSiniestro/sin_view.html')

def sinCreate(request):
    return render(request, 'ClienteSiniestro/sin_create.html')

def sinDetail(request):
    return render(request, 'ClienteSiniestro/sin_detail.html')

def sinEvid(request):
    return render(request, 'ClienteSiniestro/sin_evid.html')