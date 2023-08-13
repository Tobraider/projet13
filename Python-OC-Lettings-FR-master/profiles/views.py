import logging
from django.shortcuts import render, redirect
from .models import Profile


# Create your views here.
def index(request):
    """ View index, liste tout les profiles """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """ View detaille de profile """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logging.error("profile not found")
        return redirect('profiles:index')
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
