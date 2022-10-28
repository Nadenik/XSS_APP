from website.models import Module, Challenge
from django.contrib.auth.models import User

# function to update challenge completition progress
# challenge_progress_number is progress in binary 1=first challenge, 11=second challenge, 111, third challenge etc.
def update_user_progress(request, challenge_progress_number):
    list = request.path.split('/')
    challenge_name = list[-1]
    module_name = list[-2]

    user=User.objects.get(id=request.user.id)
    module = Module.objects.get(name=module_name, user=user)
    challenge = Challenge.objects.get(name=challenge_name, module=module)

    # update challenge progress
    challenge.is_completed = True
    challenge.save()
    # update module progress in binary 1=first challenge, 11=second challenge, 111, third challenge etc.
    int_challenge_progress_number = int(challenge_progress_number,2)
    if module.challenge_completition < int_challenge_progress_number:
        module.challenge_completition = int_challenge_progress_number
        module.save()   
