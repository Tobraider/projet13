from django.shortcuts import render
import logging


def index(request):
    """ View index du site """
    return render(request, 'index.html')


def custom_404_view(request, exception):
    """ View pour l'erreur 404 """
    return render(request, 'errors.html', status=404, context={'status': 404})


def custom_500_view(request):
    """ View pour l'erreur 500 """
    return render(request, 'errors.html', status=500, context={'status': 500})
