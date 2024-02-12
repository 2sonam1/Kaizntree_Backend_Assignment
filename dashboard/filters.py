from django_filters.rest_framework import FilterSet
from dashboard.models import Item

class ItemFilter(FilterSet):
    class Meta:
        model = Item
        fields = {
            'category' : ['exact'],
            'created_at' : ['gt','lt']
        }

