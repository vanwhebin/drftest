import django_filters
from .models import Article, Category


class ArticleFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label=u"关键词")
    category = django_filters.ModelChoiceFilter(field_name='category', queryset=Category.objects.all())
    create_date__gte = django_filters.NumberFilter(field_name='create_date', lookup_expr='year_gte', label=u'发表年份大于等于')

    class Meta:
        model = Article
        fields = {
            # "title": ['icontains'],
            # "category__name": ['icontains'],
            # "create_date": ['year__gt'],
        }
