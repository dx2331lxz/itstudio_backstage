from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
    path('register/', views.AdduserAPIView.as_view()),
    path('update/', views.UpdateAPIView.as_view()),
]
