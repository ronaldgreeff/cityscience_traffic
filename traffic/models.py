from django.db import models


class Record(models.Model):
    """ Record of traffic counts by vehicle type for a given road and year """
    year = models.IntegerField()
    count_point_ref = models.IntegerField()
    estimation_method = models.CharField(max_length=10)
    estimation_method_detailed = models.CharField(max_length=60)
    road = models.CharField(max_length=10)
    road_category = models.CharField(max_length=2)
    easting = models.IntegerField()
    latitude = models.FloatField()
    northing = models.IntegerField()
    longitude = models.FloatField()
    junc_start = models.CharField(max_length=57)
    junc_end = models.CharField(max_length=61)
    len_net_km = models.FloatField()
    len_net_mi = models.FloatField()
    AllHGVs = models.IntegerField()
    AllMotorVehicles = models.IntegerField()
    PedalCycles = models.IntegerField()
    Motorcycles = models.IntegerField()
    CarsTaxis = models.IntegerField()
    BusesCoaches = models.IntegerField()
    LightGoodsVehicles = models.IntegerField()
    V2AxleRigidHGV = models.IntegerField()
    V3AxleRigidHGV = models.IntegerField()
    V4or5AxleRigidHGV = models.IntegerField()
    V3or4AxleArticHGV = models.IntegerField()
    V5AxleArticHGV = models.IntegerField()
    V6orMoreAxleArticHGV = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.year, self.road)