from rest_framework import serializers

from apps.login.models import Department, Works, Members


class DepartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class WorksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = '__all__'


class MembersModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'
