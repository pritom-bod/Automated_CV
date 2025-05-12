from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .forms import userFrom
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

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

    return render(request, 'auth/login.html', {'form':frm})#



def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login')


#change password with old password

def change_with_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return render(request, 'auth/success.html')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'auth/pass_Change.html', {'form':form})
    else:
        return HttpResponseRedirect('login')
    

#change password without old password

def without_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user , data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return render(request, 'auth/success.html')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'auth/withoutold.html', {'form':form})
    else:
        return HttpResponseRedirect('login')
    


#success
def success(request):
    return render(request, 'auth/success.html')

