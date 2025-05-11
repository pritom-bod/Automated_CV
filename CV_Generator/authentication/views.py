from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import userFrom
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def userCreate(request):
    if request.method == 'POST':
        frm = userFrom(request.POST)
        if frm.is_valid():
            frm.save()

    else:
        frm = userFrom()   
    return render(request, 'auth/register.html', {'form':frm})

def login_from(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data= request.POST)
        if frm.is_valid():
            username = frm.cleaned_data['username']
            password = frm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'pdf/accept.html', {'form':frm})
    else:
        frm = AuthenticationForm()

    return render(request, 'auth/login.html', {'form':frm})
