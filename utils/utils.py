from website.models import ReflectedXssModule, DomBasedXssModule
from django.contrib.auth.models import User

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
        return ReflectedXssModule.objects.get(user=user)
    elif module_name == 'dom_based_xss':
        return DomBasedXssModule.objects.get(user=user)
    else:
        raise Exception(f'We have no module named {module_name}') 