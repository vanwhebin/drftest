# _*_ coding: utf-8 _*_
# @Time     :   2020/9/18 16:15
# @Author       vanwhebin

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('', views.SnippetList.as_view(), name="snippet-list"),
    path('<int:pk>', views.SnippetDetail.as_view(), name="snippet-detail"),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    path('<int:pk>/highlight/', views.SnippetHighlight.as_view(), name="snippet-highlight"),
    path('root', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
