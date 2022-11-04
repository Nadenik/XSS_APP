from website.models import ReflectedXssModule, DomBasedXssModule, StoredXssModule
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# function to update challenge completition progress
# challenge_progress_number is progress in binary 1=first challenge, 11=second challenge, 111, third challenge etc.
def update_user_progress(request, challenge_progress_number):

    list = request.path.split('/')

    module_name = list[-2]

    user = User.objects.get(id=request.user.id)
    module = get_module_object(module_name, user)
    
    # update module progress in binary 1=first challenge, 11=second challenge, 111, third challenge etc.
    int_challenge_progress_number = int(challenge_progress_number,2)
    if module.challenge_completition < int_challenge_progress_number:
        module.challenge_completition = int_challenge_progress_number
        module.save()   


# get correct module object by module_name
def get_module_object(module_name, user):
    if module_name == 'reflected_xss':
        return get_object_or_404(ReflectedXssModule, user=user)
    elif module_name == 'dom_based_xss':
        return get_object_or_404(DomBasedXssModule, user=user)
    elif module_name == 'stored_xss':
        return get_object_or_404(StoredXssModule, user=user)
    else:
        raise Exception(f'We have no module named {module_name}')

# check if challenge has been completed, returns boolean
def challenge_completed(request, required_completition_number):
    list = request.path.split('/')
    module_name = list[-2]

    user = get_object_or_404(User, id=request.user.id)
    module = get_module_object(module_name, user)
    int_required_completition_number = int(required_completition_number,2)
    if module.challenge_completition >= int_required_completition_number:
        return True
    else:
        return False
