import pytest
from django.test import RequestFactory
from django.template.loader import render_to_string
from . import views, models


@pytest.mark.django_db
@pytest.fixture(scope='function')
def createLettings():
    """ Fixture pour creer un letting """
    address = models.Address.objects.create(
        number=12,
        street='ici',
        city='la',
        state=65,
        zip_code=95400,
        country_iso_code=400
    )
    models.Letting.objects.create(title='test', address=address)


@pytest.mark.django_db
def testIndexLettingsView(createLettings):
    """ Test la vue index de lettings (status_code et bon fichier généré) """
    factory = RequestFactory()
    request = factory.get('/lettings/')
    response = views.index(request)
    assert response.status_code == 200
    expected_rendered_template = render_to_string(
        'lettings/index.html',
        {'lettings_list': models.Letting.objects.all()}
    )
    assert response.content.decode('utf-8') == expected_rendered_template


@pytest.mark.django_db
def testLettingView(createLettings):
    """ Test la vue letting (status_code et bon fichier généré) """
    factory = RequestFactory()
    request = factory.get('/lettings/1/')
    response = views.letting(request, 1)
    assert response.status_code == 200
    letting = models.Letting.objects.get(pk=1)
    expected_rendered_template = render_to_string(
        'lettings/letting.html',
        {'title': letting.title, 'address': letting.address}
    )
    assert response.content.decode('utf-8') == expected_rendered_template
