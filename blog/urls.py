from django.urls import re_path, include, path
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import routers

app_name = 'blog'


router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^articles/$', views.article_list),
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    re_path(r'^articles/filter/', views.article_search, name='article_search'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
