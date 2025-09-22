import django_filters
from django import forms
from helloworld.models import Post

class BlogFilter(django_filters.FilterSet):
    created_on = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'type': 'date'}),
        lookup_expr='date'
    )

    class Meta:
        model = Post
        fields = ['created_on']