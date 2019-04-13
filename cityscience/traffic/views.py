from traffic.serializers import VehicleCountSerializer, RecordSerializer
from traffic.models import Record, VehicleCount
from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework import viewsets


class RecordsViewSet(viewsets.ReadOnlyModelViewSet):
    """ Counts for all vehicle types by record. Filtered by record criteria. """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('year', 'estimation_method',
        'estimation_method_detailed', 'road', 'road_category',)


class VehicleCountsViewSet(viewsets.ReadOnlyModelViewSet):
    """ Counts by vehicle type. Granular filtering by record and vehicle criteria. """
    queryset = VehicleCount.objects.all().select_related('record')
    serializer_class = VehicleCountSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('vehicle_type', 'record__year', 'record__estimation_method',
        'record__estimation_method_detailed', 'record__road', 'record__road_category',)