from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User