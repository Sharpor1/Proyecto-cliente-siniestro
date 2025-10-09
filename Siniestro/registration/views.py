from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def loginView(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            login(request, form.get_user())
            return redirect('list')
        
    return render(request, 'registration/login.html', {'form':form})

def logoutView(request):
    logout(request)
    return redirect('list')