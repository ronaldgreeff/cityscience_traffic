from django.db import models

class RoadName(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.name)

class Date(models.Model):
    year = models.IntegerField()
    def __str__(self):
        return str(self.year)

class Category(models.Model):
    name = models.CharField(max_length=2)
    def __str__(self):
        return self.name

class StartJunction(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)

class EndJunction(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.name)

class BasicCountMethod(models.Model):
    method = models.CharField(max_length=10)
    def __str__(self):
        return self.method

class DetailedCountMethod(models.Model):
    method = models.CharField(max_length=60)
    def __str__(self):
        return self.method



class RoadInfo(models.Model):
    road = models.ForeignKey(RoadName, on_delete='CASCADE')
    category = models.ForeignKey(Category, on_delete='CASCADE')
    junc_start = models.ForeignKey(StartJunction, on_delete='CASCADE', related_name='junc_start')
    junc_end = models.ForeignKey(EndJunction, on_delete='CASCADE', related_name='junc_end')
    len_mi = models.FloatField()
    len_km = models.FloatField()

    def __str__(self):
        return str(self.road)

class Location(models.Model):
    count_point_ref = models.IntegerField()
    easting = models.IntegerField()
    latitude = models.FloatField()
    northing = models.IntegerField()
    longitude = models.FloatField()

    def __str__(self):
        return 'ref: {} ({}, {})'.format(self.count_point_ref, self.latitude,
            self.longitude)


class CountMethod(models.Model):
    basic_count_method = models.ForeignKey(BasicCountMethod, on_delete='CASCADE')
    detailed_count_method = models.ForeignKey(DetailedCountMethod, on_delete='CASCADE')

    def __str__(self):
        return '{}: {}'.format(str(self.basic_count_method).upper(),
            self.detailed_count_method)


class Record(models.Model):
    road = models.ForeignKey(RoadInfo, on_delete='CASCADE')
    date = models.ForeignKey(Date, on_delete='CASCADE')
    count_method = models.ForeignKey(CountMethod, on_delete='CASCADE')
    location = models.ForeignKey(Location, on_delete='CASCADE')

    def __str__(self):
        return '{}: {}'.format(self.year, self.road)

class Count(models.Model):
    record = models.OneToOneField(Record, on_delete='CASCADE')
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