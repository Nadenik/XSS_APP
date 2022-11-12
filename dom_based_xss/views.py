from django.shortcuts import render, get_object_or_404
from utils.utils import update_user_progress, challenge_completed, get_module_or_none
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from website.models import DomBasedXssModule
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Text
import json
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
    if not challenge_completed(request, '1'):
        raise PermissionDenied
    if request.method == 'GET':
        data = Text.objects.filter(dom_based_xss_module_related=get_module_or_none('dom_based_xss', request.user.id))
        context = {'texts': data}
        return render(request, 'dom_based_xss/dom_based_xss_level1.html', context)
    elif request.method == 'POST':
        update_user_progress(request, '11')
        return redirect('dom_based_xss')

@login_required
def level1_create_text(request):
    if request.method == 'POST':
        module_obj = get_module_or_none('dom_based_xss', request.user.id)
        create_data = {
            'text': request.POST.get('text'),
            'dom_based_xss_module_related': module_obj
        }
        object = Text.objects.create(**create_data)
        return JsonResponse({'id': object.pk}, status=200)

@login_required
def level1_delete_text(request, id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Text, pk=id, dom_based_xss_module_related=get_module_or_none('dom_based_xss', request.user.id))
        comment.delete()
        return HttpResponse(status=204)



