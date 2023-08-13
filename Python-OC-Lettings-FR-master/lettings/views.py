from django.shortcuts import render, redirect
from .models import Letting
import logging


def index(request):
    """ View index, liste tout les lettings """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """ View detaille de letting """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logging.error("letting not found")
        return redirect('lettings:index')
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
