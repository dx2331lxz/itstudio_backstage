from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddadministratorAPIView.as_view()),
    path('delete/', views.DeleteadministratorAPIView.as_view()),
]
