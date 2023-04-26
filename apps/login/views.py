from django.shortcuts import render, redirect
from rest_framework.views import APIView
from apps.login.models import *
# from apps.login.serializer import *
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

class AdduserAPIView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        email = data['email']
        User.objects.create_user(username=username, password=password, email=email)
        return Response({'msg': '注册成功', 'code': 200}, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        remember = data.get('remember')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            # 使用Django的login()函数进行登陆
            login(request, user)
            # 如果记住登陆，则使用全局的过期时间，默认为2周
            if remember:
                # 设置为None，则表示使用全局的过期时间
                request.session.set_expiry(None)
            else:
                # 否则设为0，关掉浏览器就注销登陆状态了
                request.session.set_expiry(0)
            # 获取next页面（原本要访问的页面，因为没登陆所以转到login页面了），如果有的话则重定向到该页面
            next_url = request.query_params.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return Response({'msg': '登录成功'}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):

    def get(self, request):
        logout(request)
        return Response({'msg': '退出登录成功', 'code': 200}, status=status.HTTP_200_OK)
