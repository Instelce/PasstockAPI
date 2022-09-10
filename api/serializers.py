from dataclasses import field
from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    email = serializers.SerializerMethodField('get_email')

    class Meta:
        model = Profile
        fields = ['url', 'username', 'email', 'image_url']

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email


class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['site_name', 'password', 'email', 'image_url', 'owner']