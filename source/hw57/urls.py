from django.urls import path

from hw57.views.base import IndexView

from hw57.views.tasks import TaskDetail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/', IndexView.as_view()),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail')
]