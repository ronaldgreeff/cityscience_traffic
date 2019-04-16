from django.db import models

# Field length reference
# [{'AADFYear': 4}, {'CP': 5}, {'Estimation_method': 9}, {'Estimation_method_detailed': 49}, {'Region': 10},
# {'LocalAuthority': 5}, {'Road': 5}, {'RoadCategory':2}, {'Easting': 6}, {'Northing': 6}, {'StartJunction': 57},
# {'EndJunction': 61}, {'LinkLength_km': 4}, {'LinkLength_miles': 5}, {'PedalCycles': 4}, {'Motorcycles': 4},
# {'CarsTaxis': 5}, {'BusesCoaches': 4}, {'LightGoodsVehicles': 5}, {'V2AxleRigidHGV': 4}, {'V3AxleRigidHGV': 3},
# {'V4or5AxleRigidHGV': 3}, {'V3or4AxleArticHGV': 4}, {'V5AxleArticHGV': 4}, {'V6orMoreAxleArticHGV': 4}, {'AllHGVs': 4},
# {'AllMotorVehicles': 6}]

class Record(models.Model):
    """ Record data: context information like time, location, data-methods, references, categories and measures """
    Y000 = 2000
    Y001 = 2001
    Y002 = 2002
    Y003 = 2003
    Y004 = 2004
    Y005 = 2005
    Y006 = 2006
    Y007 = 2007
    Y008 = 2008
    Y009 = 2009
    Y010 = 2010
    Y011 = 2011
    Y012 = 2012
    Y013 = 2013
    Y014 = 2014
    Y015 = 2015
    Y016 = 2016
    Y017 = 2017
    YEARS = ((Y000, 2000),
        (Y001, 2001),
        (Y002, 2002),
        (Y003, 2003),
        (Y004, 2004),
        (Y005, 2005),
        (Y006, 2006),
        (Y007, 2007),
        (Y008, 2008),
        (Y009, 2009),
        (Y010, 2010),
        (Y011, 2011),
        (Y012, 2012),
        (Y013, 2013),
        (Y014, 2014),
        (Y015, 2015),
        (Y016, 2016),
        (Y017, 2017),)

    year = models.IntegerField(choices=YEARS)

    count_point_ref = models.IntegerField()


    COUNTED = 0
    ESTIMATED = 1
    ESTIMATION_METHODS = (
        (COUNTED, 'Counted'),
        (ESTIMATED, 'Estimated')
    )

    estimation_method = models.IntegerField(choices=ESTIMATION_METHODS)

    MANAUL_COUNT = 0
    AUTOMATIC_COUNTER = 1
    ESTIMATED_WITH_PREV = 2
    ESTIMATED_FROM_NEAR = 3
    NEIGHBOUR_DEPENDANT = 4
    ESTIMATION_METHODS_DETAILED = ((MANAUL_COUNT, 'Manual count'),
        (AUTOMATIC_COUNTER, 'Automatic counter'),
        (ESTIMATED_WITH_PREV, 'Estimated using previous year\'s AADF on this link'),
        (ESTIMATED_FROM_NEAR, 'Estimated from nearby links'),
        (NEIGHBOUR_DEPENDANT, 'Dependent on a neighbouring counted link'),)

    estimation_method_detailed = models.IntegerField(choices=ESTIMATION_METHODS_DETAILED)

    A381 = 0
    A386 = 1
    A3125 = 2
    A3052 = 3
    A3123 = 4
    A375 = 5
    A39 = 6
    A361 = 7
    A382 = 8
    M5 = 9
    A3126 = 10
    A384 = 11
    A30 = 12
    A380 = 113
    A388 = 14
    A383 = 15
    A303 = 16
    A3072 = 17
    A3121 = 18
    A35 = 19
    A373 = 20
    A3122 = 21
    A38 = 22
    A3079 = 23
    A379 = 24
    A376 = 25
    A377 = 26
    A390 = 27
    A3124 = 28
    A3015 = 29
    A399 = 30
    A396 = 31
    A385 = 32
    A358 = 33
    ROADS = ((A381, 'A381'),
        (A386, 'A386'),
        (A3125, 'A3125'),
        (A3052, 'A3052'),
        (A3123, 'A3123'),
        (A375, 'A375'),
        (A39, 'A39'),
        (A361, 'A361'),
        (A382, 'A382'),
        (M5, 'M5'),
        (A3126, 'A3126'),
        (A384, 'A384'),
        (A30, 'A30'),
        (A380, 'A380'),
        (A388, 'A388'),
        (A383, 'A383'),
        (A303, 'A303'),
        (A3072, 'A3072'),
        (A3121, 'A3121'),
        (A35, 'A35'),
        (A373, 'A373'),
        (A3122, 'A3122'),
        (A38, 'A38'),
        (A3079, 'A3079'),
        (A379, 'A379'),
        (A376, 'A376'),
        (A377, 'A377'),
        (A390, 'A390'),
        (A3124, 'A3124'),
        (A3015, 'A3015'),
        (A399, 'A399'),
        (A396, 'A396'),
        (A385, 'A385'),
        (A358, 'A358'),)

    road = models.IntegerField(choices=ROADS)

    TA = 0
    PA = 1
    TM = 2
    ROAD_CATEGORIES = ((TA, 'TA'),
        (PA, 'PA'),
        (TM, 'TM'),)

    road_category = models.IntegerField(choices=ROAD_CATEGORIES)

    easting = models.IntegerField()
    latitude = models.FloatField()
    northing = models.IntegerField()
    longitude = models.FloatField()

    junc_start = models.CharField(max_length=57)
    junc_end = models.CharField(max_length=61)
    len_net_km = models.FloatField()
    len_net_mi = models.FloatField()

    def __str__(self):
        return '{}: {}'.format(self.year, self.get_road_display())


class VehicleCount(models.Model):
    """ Vehicle count data: counts by vehicle type """
    record = models.ForeignKey(Record, on_delete='CASCADE')

    ALLHGVS = 0
    ALLMOTORVEHICLES = 1
    PEDALCYCLES = 2
    MOTORCYCLES = 3
    CARSTAXIS = 4
    BUSESCOACHES = 5
    LIGHTGOODSVEHICLES = 6
    V2AXLERIGIDHGV = 7
    V3AXLERIGIDHGV = 8
    V4OR5AXLERIGIDHGV = 9
    V3OR4AXLEARTICHGV = 10
    V5AXLEARTICHGV = 11
    V6ORMOREAXLEARTICHGV = 12
    VEHICLE_TYPES = ((ALLHGVS, 'AllHGVs'),
        (ALLMOTORVEHICLES, 'AllMotorVehicles'),
        (PEDALCYCLES, 'PedalCycles'),
        (MOTORCYCLES, 'Motorcycles'),
        (CARSTAXIS, 'CarsTaxis'),
        (BUSESCOACHES, 'BusesCoaches'),
        (LIGHTGOODSVEHICLES, 'LightGoodsVehicles'),
        (V2AXLERIGIDHGV, 'V2AxleRigidHGV'),
        (V3AXLERIGIDHGV, 'V3AxleRigidHGV'),
        (V4OR5AXLERIGIDHGV, 'V4or5AxleRigidHGV'),
        (V3OR4AXLEARTICHGV, 'V3or4AxleArticHGV'),
        (V5AXLEARTICHGV, 'V5AxleArticHGV'),
        (V6ORMOREAXLEARTICHGV, 'V6orMoreAxleArticHGV'),)

    vehicle_type = models.IntegerField(choices=VEHICLE_TYPES)

    count = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.vehicle_count_type, self.count)