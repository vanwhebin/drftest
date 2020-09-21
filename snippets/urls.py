# _*_ coding: utf-8 _*_
# @Time     :   2020/9/18 16:15
# @Author       vanwhebin

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:pk>', snippet_detail, name="snippet-detail"),
    # path('users/', user_list, name="user-list"),
    # path('users/<int:pk>/', user_detail, name="user-detail"),
    # path('<int:pk>/highlight/', snippet_highlight, name="snippet-highlight"),
    # path('root', views.api_root),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
