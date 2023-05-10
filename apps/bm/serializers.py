from rest_framework import serializers

from apps.login.models import NewMember, History, Comments


class NewMemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewMember
        fields = '__all__'


class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


# class CommentsModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comments
#         fields = '__all__'
