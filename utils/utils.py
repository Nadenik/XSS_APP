from website.models import ReflectedXssModule, DomBasedXssModule, StoredXssModule
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404

# function to update challenge completition progress
# challenge_progress_number is progress in binary 1=first challenge, 11=second challenge, 111, third challenge etc.
def update_user_progress(request, challenge_progress_number):

    list = request.path.split('/')

    module_name = list[-2]

    user = User.objects.get(id=request.user.id)
    module = get_module_or_none(module_name, user)
    
    # update module progress in binary 1=first challenge, 11=second challenge, 111, third challenge etc.
    int_challenge_progress_number = int(challenge_progress_number,2)
    if module.challenge_completition < int_challenge_progress_number:
        module.challenge_completition = int_challenge_progress_number
        module.save()   


# get correct module object by module_name, returns None if object does not exsist
def get_module_or_none(module_name, user):
    if module_name == 'reflected_xss':
        return ReflectedXssModule.objects.filter(user=user).first()
    elif module_name == 'dom_based_xss':
        return DomBasedXssModule.objects.filter(user=user).first()
    elif module_name == 'stored_xss':
        return StoredXssModule.objects.filter(user=user).first()
    else:
        raise Exception(f'We have no module named {module_name}')

# check if challenge has been completed, returns boolean
def challenge_completed(request, required_completition_number):
    list = request.path.split('/')
    module_name = list[-2]

    user = get_object_or_404(User, id=request.user.id)
    try:
        module = get_module_or_none(module_name, user)
    except:
        raise Http404
    int_required_completition_number = int(required_completition_number,2)
    if module.challenge_completition >= int_required_completition_number:
        return True
    else:
        return False

# returns true if there is a need to display rules to user(if any module is started return false)

def read_rules(user):
    if ReflectedXssModule.objects.filter(user = user).exists() or DomBasedXssModule.objects.filter(user = user).exists() or StoredXssModule.objects.filter(user = user).exists():
        return False
    else:
        return True