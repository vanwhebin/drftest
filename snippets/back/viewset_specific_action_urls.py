# _*_ coding: utf-8 _*_
# @Time     :   2020/9/18 16:15
# @Author       vanwhebin

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from snippets import views

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', snippet_list, name="snippet-list"),
    path('<int:pk>', snippet_detail, name="snippet-detail"),
    path('users/', user_list, name="user-list"),
    path('users/<int:pk>/', user_detail, name="user-detail"),
    path('<int:pk>/highlight/', snippet_highlight, name="snippet-highlight"),
    path('root', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
