from traffic.serializers import DataSerializer
from traffic.models import Record
from django_filters import rest_framework as filters
from django.shortcuts import render
from rest_framework import viewsets


class RecordViewSet(viewsets.ReadOnlyModelViewSet)    :
    """ List of all traffic count records """
    queryset = Record.objects.all()
    serializer_class = DataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ["id", "year", "count_point_ref", "estimation_method",
        "estimation_method_detailed", "road", "road_category", "easting", "latitude",
        "northing", "longitude", "junc_start", "junc_end", "len_net_km", "len_net_mi"]