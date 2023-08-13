import pytest
from django.test import RequestFactory
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from . import views, models


@pytest.mark.django_db
@pytest.fixture(scope='function')
def createProfiles():
    """ Fixture pour creer un profile """
    user = User.objects.create_user(username='testuser', password='testpassword')
    models.Profile.objects.create(user=user, favorite_city='test')


@pytest.mark.django_db
def testIndexProfilesView(createProfiles):
    """ Test la vue index de profiles (status_code et bon fichier généré) """
    factory = RequestFactory()
    request = factory.get('/profiles/')
    response = views.index(request)
    assert response.status_code == 200
    expected_rendered_template = render_to_string(
        'profiles/index.html',
        {'profiles_list': models.Profile.objects.all()}
    )
    assert response.content.decode('utf-8') == expected_rendered_template


@pytest.mark.django_db
def testProfileView(createProfiles):
    """ Test la vue profile (status_code et bon fichier généré) """
    factory = RequestFactory()
    request = factory.get('/profiles/testuser/')
    response = views.profile(request, "testuser")
    assert response.status_code == 200
    profile = models.Profile.objects.get(user__username="testuser")
    expected_rendered_template = render_to_string('profiles/profile.html', {'profile': profile})
    assert response.content.decode('utf-8') == expected_rendered_template
