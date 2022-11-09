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
        return redirect('stored_xss_level1')

@login_required
def level2_view(request):
    if not challenge_completed(request, '11'):
        raise PermissionDenied
    mydata = Comment.objects.filter(challenge_assigned='2', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
    context = {'comments': mydata}
    return render(request, 'stored_xss/level2.html', context)

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
        return redirect('stored_xss_level2')

def level3_view(request):
    if request.method == 'GET':
        mydata = Image.objects.filter(stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        context = {'images': mydata}
        return render(request, 'stored_xss/level3.html', context)

def level3_image_endpoint(request):
    if request.method == 'POST':
        module_obj = get_module_or_none('stored_xss', request.user.id)
        image = request.FILES['image']

        info_dict = {"Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)}

        for label,value in info_dict.items():
            print(f"{label:25}: {value}")
        exifdata = image.getexif()
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes 
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")
        create_data = {
            'image': image,
            'stored_xss_module_related': module_obj
        }
        Image.objects.create(**create_data)

        return redirect('stored_xss_level3')


# delete comment, returns 204 no content
@login_required
def level1_delete_comment(request, id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=id, challenge_assigned='1', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        comment.delete()
        return HttpResponse(status=204)

def level2_delete_comment(request, id):
    if request.method == 'DELETE':
        comment = get_object_or_404(Comment, pk=id, challenge_assigned='2', stored_xss_module_related=get_module_or_none('stored_xss', request.user.id))
        comment.delete()
        return HttpResponse(status=204)
