from rest_framework import serializers
from .models import Article, Category
from django.contrib.auth import get_user_model

User = get_user_model()


# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=True, allow_blank=True, max_length=255)
#     body = serializers.CharField(required=False, allow_blank=True)
#     author = serializers.ReadOnlyField(source='author.id')
#     status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
#     create_date = serializers.DateField(read_only=True)
#
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.body = validated_data.get('body', instance.body)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'author', 'create_date')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
