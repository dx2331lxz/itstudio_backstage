from apps.bm import views
from django.urls import path

urlpatterns = [

    # 报名人员管理
    path('registrant/', views.RegistrantView.as_view()),
    path('registrant/delete/', views.RegistrantDeleteView.as_view()),

    # 历史表
    path('history/', views.HistoryView.as_view()),
    path('history/delete/', views.HistoryDeleteView.as_view()),

    # # 弹幕
    # path('comments/', views.CommentsView.as_view()),

]
