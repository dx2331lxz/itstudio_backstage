from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.GetadministratorAPIView.as_view()),
    path('delete/', views.DeleteadministratorAPIView.as_view()),
]
