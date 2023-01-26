from django.shortcuts import render, redirect
from .models import StoredXssModule
from django.contrib.auth.models import User
from .models import Comment, Image
from utils.utils import get_module_or_none, update_user_progress, challenge_completed
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from PIL import Image as Im
from PIL.ExifTags import TAGS

@login_required
def stored_xss_view(request):
    if request.method == 'GET':
        user=User.objects.get(id=request.user.id)
        module, created = StoredXssModule.objects.get_or_create(user=user)
        context = {"module": module}
        return render(request, 'stored_xss/stored_xss.html', context)

@login_required
def introduction_view(request):
    if request.method == 'GET':
        return render(request, 'stored_xss/introduction.html', {})
    if request.method == 'POST':
        update_user_progress(request, '1')
        return redirect('stored_xss')

@login_required
def level1_view(request):
    if not challenge_completed(request, '1'):
        raise PermissionDenied
    if request.method == 'GET':
        mydata = Comment.objects.filter(challenge_assigned='1', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        context = {'comments': mydata}
        return render(request, 'stored_xss/level1.html', context)
    elif request.method == 'POST':
        # update challenge progress
        update_user_progress(request, '11')
        return HttpResponse(status=204)

@login_required
def level1_create_comment(request):
    if not challenge_completed(request, '1'):
        raise PermissionDenied
    if request.method == 'POST':
        module_obj = get_module_or_none('stored_xss', request.user.id)
        create_data = {
            'comment': request.POST['comment'],
            'stored_xss_module_related': module_obj,
            'challenge_assigned': '1',
        }
        Comment.objects.create(**create_data)
        return redirect('/learn/stored_xss/level1#comment')

@login_required
def level2_view(request):
    if not challenge_completed(request, '11'):
        raise PermissionDenied
    if request.method == 'GET':
        mydata = Comment.objects.filter(challenge_assigned='2', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        context = {'comments': mydata}
        return render(request, 'stored_xss/level2.html', context)
    elif request.method == 'POST':
        # update challenge progress
        update_user_progress(request, '111')
        return HttpResponse(status=204)

@login_required
def level2_create_comment(request):
    if not challenge_completed(request, '11'):
        raise PermissionDenied
    if request.method == 'POST':
        module_obj = get_module_or_none('stored_xss', request.user.id)
        create_data = {
            'comment': request.POST['comment'],
            'stored_xss_module_related': module_obj,
            'challenge_assigned': '2',
        }
        Comment.objects.create(**create_data)
        return redirect('/learn/stored_xss/level2#comment')

@login_required
def level3_view(request):
    if not challenge_completed(request, '111'):
        raise PermissionDenied
    if request.method == 'GET' and 'search' in request.GET:
        search_query = request.GET.get('search')
        mydata = Image.objects.filter(description__contains=search_query, 
        stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        context = {'images': mydata,
        'query': search_query}
        return render(request, 'stored_xss/level3.html', context)
    elif request.method == 'POST':
        # update challenge progress
        update_user_progress(request, '1111')
        return HttpResponse(status=204)
    else:
        mydata = Image.objects.filter(stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        context = {'images': mydata}
        return render(request, 'stored_xss/level3.html', context)

@login_required
def level3_image_endpoint(request):
    if not challenge_completed(request, '111'):
        raise PermissionDenied
    if request.method == 'POST':
        try:
            image = request.FILES['image']
        except:
            return redirect('stored_xss_level3')
        module_obj = get_module_or_none('stored_xss', request.user.id)
        description = request.POST['description']
        create_data = {
            'image': image,
            'stored_xss_module_related': module_obj,
            'description': description
        }
        x = Image.objects.create(**create_data)
        # if exif Artist exists add it to database
        if x.exif():
            x.artist = x.exif()
            x.save()

        return redirect('stored_xss_level3')


# delete comment, returns 204 no content
@login_required
def level1_delete_comment(request, id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=id, challenge_assigned='1', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        comment.delete()
        return HttpResponse(status=204)

@login_required
def level2_delete_comment(request, id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=id, challenge_assigned='2', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        comment.delete()
        return HttpResponse(status=204)

@login_required
def level3_delete_image(request, id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Image, pk=id, stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        comment.delete()
        return HttpResponse(status=204)