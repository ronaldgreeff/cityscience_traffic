import os
import django
import pandas as pd
from convertbng.util import convert_lonlat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cityscience.settings')
django.setup()


from traffic.models import Record


df = pd.read_csv('Devon.csv')


def convert_to_lonlat(easting, northing):

    eastings = [easting]
    northings = [northing]

    rle = convert_lonlat(eastings, northings)
    return rle[1][0], rle[0][0]


def create_records(_print=True):

    record_objects = []
    for row in df.to_dict(orient='records'):

        latitude, longitude = convert_to_lonlat(row['Easting'], row['Northing'])

        record_objects.append(Record(
                estimation_method = row['Estimation_method'],
                estimation_method_detailed = row['Estimation_method_detailed'],
                road = row['Road'],
                road_category = row['RoadCategory'],
                year = row['AADFYear'],
                count_point_ref = row['CP'],
                easting = row['Easting'],
                northing = row['Northing'],
                latitude = latitude,
                longitude = longitude,
                junc_start = row['StartJunction'],
                junc_end = row['EndJunction'],
                len_net_km = row['LinkLength_km'],
                len_net_mi = row['LinkLength_miles'],
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
        )

    Record.objects.bulk_create(record_objects)
    print('{} records succesfully created'.format(len(record_objects)))

create_records()