from rest_framework import serializers
from apps.login.models import *
from django.contrib.auth.models import User


class GetadministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

