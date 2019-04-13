from traffic.models import Record, VehicleCount
from rest_framework import serializers


class VehicleCountSerializer(serializers.ModelSerializer):
    """ Serializes records """
    vehicle_type = serializers.CharField(source='get_vehicle_type_display') # make this nested -> DRY
    year = serializers.IntegerField(source='record.year')

    junc_start = serializers.CharField(source='record.junc_start')
    junc_end = serializers.CharField(source='record.junc_end')
    len_net_km = serializers.IntegerField(source='record.len_net_km')
    len_net_mi = serializers.IntegerField(source='record.len_net_mi')
    count_point_ref = serializers.IntegerField(source='record.count_point_ref')

    estimation_method = serializers.CharField(source='record.get_estimation_method_display')
    estimation_method_detailed = serializers.CharField(source='record.get_estimation_method_detailed_display')
    road = serializers.CharField(source='record.get_road_display')
    road_category = serializers.CharField(source='record.get_road_category_display')

    class Meta:
        model = VehicleCount
        exclude = ('id', 'record',)



class RecordVehicleTypeSerializer(serializers.ModelSerializer):
    """ Serializes vehicle counts by vehicle type - nested within the record serializer """
    vehicle_type = serializers.CharField(source='get_vehicle_type_display')#source='get_vehicle_type_display')
    class Meta:
        model = VehicleCount
        exclude = ('id', 'record')


class RecordSerializer(serializers.ModelSerializer):
    """ Serializes record data and nests the related vehicle counts within it"""
    vehicle_counts = RecordVehicleTypeSerializer(source='vehiclecount_set', many=True)

    class Meta:
        model = Record
        exclude = ('id', 'northing', 'easting', 'year', 'estimation_method',
        'estimation_method_detailed', 'road_category', 'road')