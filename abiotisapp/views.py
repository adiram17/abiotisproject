from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Abiotis
from .forms import AbiotisForm

@login_required
def home(request):
    return render(request, 'pages/home.html', {})

def test(request):
    return render(request, 'pages/test.html', {})

@login_required
def profile(request):
    return render(request, 'user/profile.html', {})

@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Update Password Success.')
            return redirect('home')
        else:
            messages.error(request, 'Update Password Canceled.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })

@login_required
def abiotisList(request, type):
    print(type)
    if type!='':
        abiotis=Abiotis.objects.filter(type=type)
        print(abiotis)
        return render(request, 'pages/abiotis_list.html', {'abiotis':abiotis, 'type':type})

@login_required
def abiotisCreate(request, type):
    if request.method == "POST":  
        form = AbiotisForm(request.POST)
        if form.is_valid():  
            try: 
                abiotis = form.instance
                abiotis.save()
                messages.success(request, "Data berhasil disimpan. ")
                return redirect('/abiotis_list/'+type)  
            except Exception as e:  
                messages.error(request, "Data gagal disimpan.\n"+str(e))
                return redirect('/abiotis_list/'+type)  
    else:  
        form = AbiotisForm(initial={'type':type})  
    return render(request,'pages/abiotis_create.html',{'form':form}) 

@login_required
def abiotisDetail(request, type, id):
    abiotis = Abiotis.objects.get(id=id, type=type)
    return render(request, 'pages/abiotis_detail.html', {'abiotis':abiotis, 'type':type})

