from django.shortcuts import render, HttpResponse, redirect
from .forms import MyUserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from utils.utils import get_module_or_none, read_rules


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
        return render(request, 'registration/sign_up.html', {'form': form}) 


def index(request):
    reflected_xss_object = get_module_or_none('reflected_xss', request.user.id)
    stored_xss_object = get_module_or_none('stored_xss', request.user.id)
    dom_xss_object = get_module_or_none('dom_based_xss', request.user.id)
    context = {
        'reflected_xss': reflected_xss_object,
        'stored_xss': stored_xss_object,
        'dom_based_xss': dom_xss_object
    }
    return render(request, 'website/index.html', context)

@login_required
def learn_view(request):
    context = {}
    # check if there is a need to show rules to user
    if read_rules(request.user) == True:
        context.update({'rules': True})
    return render(request, 'website/learn.html', context)

@login_required
def profile_view(request):
    reflected_xss_object = get_module_or_none('reflected_xss', request.user.id)
    stored_xss_object = get_module_or_none('stored_xss', request.user.id)
    dom_xss_object = get_module_or_none('dom_based_xss', request.user.id)
    context = {
        'reflected_xss': reflected_xss_object,
        'stored_xss': stored_xss_object,
        'dom_based_xss': dom_xss_object
    }
    return render(request, 'website/profile.html', context)

@login_required
def rules_view(request):
    return render(request, 'website/rules.html', {})