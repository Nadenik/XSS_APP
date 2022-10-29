from django.shortcuts import render
from utils.utils import update_user_progress
from django.http import HttpResponseRedirect
from django.urls import reverse
from website.models import DomBasedXssModule
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dom_based_xss_view(request):
    user=User.objects.get(id=request.user.id)
    module, created = DomBasedXssModule.objects.get_or_create(user=user)
    context = {"module": module}
    return render(request, 'dom_based_xss/dom_based_xss.html', context)

@login_required
def dom_based_xss_introduction(request):
    if request.method == 'GET':
        return render(request, 'dom_based_xss/dom_based_xss_introduction.html', {})
    if request.method == 'POST':
        update_user_progress(request, '1')
        return HttpResponseRedirect(reverse('dom_based_xss'))

@login_required
def dom_based_xss_level1(request):
    if request.method == 'GET':
        return render(request, 'dom_based_xss/dom_based_xss_level1.html', {})
    elif request.method == 'POST':
        update_user_progress(request, '11')
        return redirect('dom_based_xss')
