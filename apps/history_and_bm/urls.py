from django.urls import path
from . import views

urlpatterns = [
    path('works/', views.WorksAPIView.as_view()),
    path('department/', views.DepartmentAPIView.as_view()),
    path('members/', views.MembersAPIView.as_view()),
]
