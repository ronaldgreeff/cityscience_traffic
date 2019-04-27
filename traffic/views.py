from traffic.serializers import *
from traffic.models import *
from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework import viewsets


class CountViewSet(viewsets.ReadOnlyModelViewSet):
    """ List of all traffic count Counts """
    queryset = Record.objects.all().select_related('count')
    serializer_class = RecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('road', 'date', 'count_method', 
        'count_method__basic_count_method',
        'count_method__detailed_count_method', 'location',
        'road__category', 'road__junc_start', 'road__junc_end', 

        'road__road__name',
        'date__year', 'location__count_point_ref',
        'road__category__name', 'road__junc_start__name',
        'road__junc_end__name',
    )