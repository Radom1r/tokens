from django_filters import rest_framework as filters
from .models import Advertisement
from django.contrib.auth.models import User

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateTimeFromToRangeFilter()
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
