from rest_framework import serializers

from apps.login.models import NewMember

class NewMemberModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewMember
        fields = '__all__'
