from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ Modele profile les champs sont : user, favorite_city """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="+")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
