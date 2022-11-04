from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from website.models import ReflectedXssModule
from django.contrib.auth.models import User
from utils.utils import update_user_progress, challenge_completed
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# main reflected xss module page
@login_required
def reflected_xss_view(request):
    if request.method == 'GET':
        user=User.objects.get(id=request.user.id)
        module, created = ReflectedXssModule.objects.get_or_create(user=user)
        context = {"module": module}
        return render(request, 'reflected_xss/reflected_xss.html', context)

# introduction
@login_required
def introduction_view(request):
    if request.method == 'GET':
        return render(request, 'reflected_xss/introduction.html', {})
    if request.method == 'POST':
        update_user_progress(request, '1')
        return redirect('reflected_xss')
# level one
@login_required
def level1_view(request):
    if not challenge_completed(request, '1'):
        raise PermissionDenied
    if request.method == 'GET' and 'search' not in request.GET:
        context = {
            'completed': challenge_completed(request, '11')
        }
        return render(request, 'reflected_xss/level1.html', context)

    elif request.method == 'GET' and 'search' in request.GET:
        context = {
            "search":request.GET.get("search"),
            'completed': challenge_completed(request, '11')
        }
        return render(request, 'reflected_xss/level1.html', context)

    elif request.method == 'POST':
        # update challenge progress
        update_user_progress(request, '11')
        return HttpResponse(status=204)
# level two
@login_required
def level2_view(request):
    if not challenge_completed(request, '11'):
        raise PermissionDenied
    if request.method == 'GET' and 'search' not in request.GET:
        return render(request, 'reflected_xss/level2.html', {})

    elif request.method == 'GET' and 'search' in request.GET:
        context = {
            "search":request.GET.get("search")
        }
        return render(request, 'reflected_xss/level2.html', context)

    elif request.method == 'POST':
        # update challenge progress
        update_user_progress(request, '111')
        return HttpResponseRedirect(reverse('reflected_xss'))
