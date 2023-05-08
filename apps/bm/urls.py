from apps.bm import views
from django.urls import path

urlpatterns = [
    path('', views.RegistantView.as_view()),
    path('delete/', views.RegistantDeleteView.as_view()),

]