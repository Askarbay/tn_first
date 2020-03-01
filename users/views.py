from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Profile



# Create your views here.
def index(request):#создаем свою функцию
    context = {}#с помощью словаря можем передать модель и форму в шаблон HTML
    return render(request, 'index.html', context)#собственно вызываем шаблон HTML



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse("User is not active")
            else:
                return HttpResponse("User is None")
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            
            user_form.save()
            profile_form.save()
            
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'edit_profile.html', context)

def profile(request):
    return render(request, 'profile.html')


def edit_tarif(request):
    if request.method == 'POST':
        tarif_form = TarifEditForm(data=request.POST or None, instance=request.user.profile)
        if tarif_form.is_valid():
            tarif_form.save()

    else:
        tarif_form = TarifEditForm(instance=request.user.profile)

    context = {
        'tarif_form': tarif_form,
    }
    return render(request, 'edit_tarif.html', context)