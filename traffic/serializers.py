from traffic.models import *
from rest_framework import serializers

class DateSerializer(serializers.ModelSerializer):
    year = serializers.IntegerField()

    class Meta:
        model = Date
        exclude = ('id',)

class RoadSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    category = serializers.CharField()
    junc_start = serializers.CharField()
    junc_end = serializers.CharField()
    len_mi = serializers.FloatField()
    len_km = serializers.FloatField()

    class Meta:
        model = Road
        exclude = ('id',)

class LocationSerializer(serializers.ModelSerializer):
    count_point_ref = serializers.IntegerField()
    easting = serializers.IntegerField()
    latitude = serializers.FloatField()
    northing = serializers.IntegerField()
    longitude = serializers.FloatField()

    class Meta:
        model = Location
        exclude = ('id',)

class CountMethodSerializer(serializers.ModelSerializer):
    basic_count_method = serializers.CharField()
    detailed_count_method = serializers.CharField()

    class Meta:
        model = CountMethod
        exclude = ('id',)


class CountSerializer(serializers.ModelSerializer):

    AllHGVs = serializers.IntegerField()
    AllMotorVehicles = serializers.IntegerField()
    PedalCycles = serializers.IntegerField()
    Motorcycles = serializers.IntegerField()
    CarsTaxis = serializers.IntegerField()
    BusesCoaches = serializers.IntegerField()
    LightGoodsVehicles = serializers.IntegerField()
    V2AxleRigidHGV = serializers.IntegerField()
    V3AxleRigidHGV = serializers.IntegerField()
    V4or5AxleRigidHGV = serializers.IntegerField()
    V3or4AxleArticHGV = serializers.IntegerField()
    V5AxleArticHGV = serializers.IntegerField()
    V6orMoreAxleArticHGV = serializers.IntegerField()

    class Meta:
        model = Count
        exclude = ('id', 'record')

class RecordSerializer(serializers.ModelSerializer):
    road = RoadSerializer()
    date = DateSerializer()
    count_method = CountMethodSerializer()
    location = LocationSerializer()
    count = CountSerializer()

    class Meta:
        model = Record
        exclude = ('id',)