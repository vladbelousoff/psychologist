import django_filters
from .models import Question


class QuestionFilter(django_filters.FilterSet):
    language = django_filters.CharFilter(field_name='language__name', lookup_expr='iexact')

    class Meta:
        model = Question
        fields = ['language']
