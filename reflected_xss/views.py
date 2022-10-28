from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from website.models import Module, Challenge
from django.contrib.auth.models import User
from utils.utils import update_user_progress

# Create your views here.

def reflected_xss_view(request):
    user=User.objects.get(id=request.user.id)
    module = Module.objects.get(name='reflected_xss', user=user)
    context = {"module": module}    
    return render(request, 'reflected_xss/reflected_xss.html', context)

def introduction_view(request):
    if request.method == 'GET':
        return render(request, 'reflected_xss/introduction.html', {})
    if request.method == 'POST':
        update_user_progress(request, '1')
        return HttpResponseRedirect(reverse('reflected_xss'))


def level1_view(request):

    if request.method == 'GET' and 'search' not in request.GET:
        return render(request, 'reflected_xss/level1.html', {})

    elif request.method == 'GET' and 'search' in request.GET:
        context = {
            "search":request.GET.get("search")
        }
        return render(request, 'reflected_xss/level1.html', context)

    elif request.method == 'POST':
        # update challenge progress
        update_user_progress(request, '11')
        return HttpResponseRedirect(reverse('reflected_xss'))
