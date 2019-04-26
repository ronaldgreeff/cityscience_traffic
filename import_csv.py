import os
import django
import pandas as pd
from convertbng.util import convert_lonlat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cityscience.settings')
django.setup()


from traffic.models import *


df = pd.read_csv('Devon.csv')


def convert_to_lonlat(easting, northing):

    eastings = [easting]
    northings = [northing]

    rle = convert_lonlat(eastings, northings)
    return rle[1][0], rle[0][0]


def create_records(_print=True):

    database_objects = []
    for c, row in enumerate(df.to_dict(orient='records')):
        if c < 10:

            latitude, longitude = convert_to_lonlat(row['Easting'], row['Northing'])

            date_obj, _ = Date.objects.get_or_create(year = row['AADFYear'])
            category_obj, _ = Category.objects.get_or_create(name = row['RoadCategory'])
            junc_start_obj, _ = StartJunction.objects.get_or_create(name = row['StartJunction'])
            junc_end_obj, _ = EndJunction.objects.get_or_create(name = row['EndJunction'])
            bcm_obj, _ = BasicCountMethod.objects.get_or_create(method=row['Estimation_method'])
            dcm_obj, _ = DetailedCountMethod.objects.get_or_create(method = row['Estimation_method_detailed'],)
            road_obj, _ = Road.objects.get_or_create(
                name = row['Road'],
                category = category_obj,
                junc_start = junc_start_obj,
                junc_end = junc_end_obj,
                len_mi = row['LinkLength_miles'],
                len_km = row['LinkLength_km'],
                )
            location_obj, _ = Location.objects.get_or_create(
                count_point_ref = row['CP'],
                easting = row['Easting'],
                latitude = latitude,
                northing = row['Northing'],
                longitude = longitude,
                )
            count_method_obj, _ = CountMethod.objects.get_or_create(
                basic_count_method = bcm_obj,
                detailed_count_method = dcm_obj,
                )
            record_obj, _ = Record.objects.get_or_create(
                road = road_obj,
                date = date_obj,
                count_method = count_method_obj,
                location = location_obj,
                )
            count_obj, _ = Count.objects.get_or_create(
                record = record_obj,
                AllHGVs = row['AllHGVs'],
                AllMotorVehicles = row['AllMotorVehicles'],
                PedalCycles = row['PedalCycles'],
                Motorcycles = row['Motorcycles'],
                CarsTaxis = row['CarsTaxis'],
                BusesCoaches = row['BusesCoaches'],
                LightGoodsVehicles = row['LightGoodsVehicles'],
                V2AxleRigidHGV = row['V2AxleRigidHGV'],
                V3AxleRigidHGV = row['V3AxleRigidHGV'],
                V4or5AxleRigidHGV = row['V4or5AxleRigidHGV'],
                V3or4AxleArticHGV = row['V3or4AxleArticHGV'],
                V5AxleArticHGV = row['V5AxleArticHGV'],
                V6orMoreAxleArticHGV = row['V6orMoreAxleArticHGV'],
                )

            print('{}, {}'.format(longitude, latitude))

create_records()