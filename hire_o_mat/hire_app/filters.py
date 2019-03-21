import django_filters
from django import forms
from .models import City, Position, Skill, UserProfile

class UserProfileFilter(django_filters.FilterSet):
    city = django_filters.ModelMultipleChoiceFilter(queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    skills = django_filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = UserProfile
        fields = ['city', 'skills', ]

class PositionFilter(django_filters.FilterSet):
    position = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Position
        fields = ['position', 'company',]
