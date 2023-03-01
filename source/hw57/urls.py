from django.urls import path

from hw57.views.base import IndexView, IndexRedirectView

from hw57.views.issues import IssueDetail, IssueUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='issue_index_redirect'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
]
