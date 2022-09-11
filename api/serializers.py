from rest_framework import serializers

from .models import *


class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['site_name', 'password', 'email', 'image_url', 'owner']