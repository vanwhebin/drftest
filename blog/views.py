from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.core.paginator import Paginator


from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer
from .filters import ArticleFilter


@api_view(['GET', 'POST'])
def article_list(request, format=None):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def article_detail(request, pk, format=None):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def article_search(request):
    f = ArticleFilter(request.GET, queryset=Article.objects.filter(status='p'))
    paginator = Paginator(f.qs, 3)
    page = request.GET.get('page')
    pagination = paginator.get_page(page)
    context = {"filter": f, 'pagination': pagination, "paginator": paginator, "is_paginated": True}
    return render(request, 'blog/article_search.html', context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
