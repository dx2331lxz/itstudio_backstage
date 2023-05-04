from django.shortcuts import render
from rest_framework.views import APIView
from apps.login.models import *
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import GetadministratorSerializer


# Create your views here.

# 查看管理人员信息

class GetadministratorAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = GetadministratorSerializer(instance=user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteadministratorAPIView(APIView):
    def post(self, request):
        uid = request.data.get('id', '')
        if uid == '':
            return Response({'msg': '请携带id', 'code': 403}, status=status.HTTP_403_FORBIDDEN)
        User.objects.filter(id=uid).delete()
        return Response({'msg': '删除成功', 'code': 200}, status=status.HTTP_200_OK)
