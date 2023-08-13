from django.test import RequestFactory
from django.template.loader import render_to_string
from django.urls import reverse
from django.test import Client
from . import views


def testIndexView():
    """ Test la vue index du site (status_code et bon fichier généré) """
    factory = RequestFactory()
    request = factory.get('/')
    response = views.index(request)
    assert response.status_code == 200
    expected_rendered_template = render_to_string('index.html')
    assert response.content.decode('utf-8') == expected_rendered_template


def testAdminAccessible():
    """ Test si l'interface d'administration est joingnable """
    client = Client()
    url = reverse('admin:login')
    response = client.get(url)
    assert response.status_code == 200


def testError404():
    """ Test si l'erreur 404 retourne le bon html """
    client = Client()
    response = client.get('fjrfgker')
    assert response.status_code == 404
    expected_rendered_template = render_to_string('errors.html', {'status': 404})
    assert response.content.decode('utf-8') == expected_rendered_template
