from django.conf import settings
from django.db import models


class Password(models.Model):
    site_name = models.CharField(max_length=40)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=400, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.site_name} Password - {self.owner}'
