from django.shortcuts import render, HttpResponse, redirect
from .forms import MyUserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from utils.utils import get_module_object


def sign_up_view(request):

    if request.method == 'GET':
        form = MyUserCreationForm
        return render(request, 'registration/sign_up.html', {'form':form})
    elif request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('home'))
        else:
            return HttpResponseRedirect('/')


def index(request):
    return render(request, 'website/index.html', {})

@login_required
def learn_view(request):
    return render(request, 'website/learn.html', {})

@login_required
def profile_view(request):
    reflected_xss_object = get_module_object('reflected_xss', request.user.id)
    context = {
        'reflected_xss': reflected_xss_object
    }
    return render(request, 'website/profile.html', context)    