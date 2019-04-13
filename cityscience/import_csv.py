import os
import django
import pandas as pd
from convertbng.util import convert_lonlat
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cityscience.settings')
django.setup()


from traffic.models import Record, VehicleCount


df = pd.read_csv('Devon.csv')


def convert_to_lonlat(easting, northing):

    eastings = [easting]
    northings = [northing]

    rle = convert_lonlat(eastings, northings)
    return rle[1][0], rle[0][0]


def create_records():

    for c, row in enumerate(df.to_dict(orient='records')):

        easting = row['Easting']
        northing = row['Northing']
        coord_x, coord_y = convert_to_lonlat(easting, northing)

        vehicle_types = ['AllHGVs', 'AllMotorVehicles', 'PedalCycles', 'Motorcycles', 'CarsTaxis',
        'BusesCoaches', 'LightGoodsVehicles', 'V2AxleRigidHGV', 'V3AxleRigidHGV',
        'V4or5AxleRigidHGV', 'V3or4AxleArticHGV', 'V5AxleArticHGV']

        r, s1 = Record.objects.get_or_create(
            year = dict(map(reversed, Record.YEARS))[row['AADFYear']],
            estimation_method = dict(map(reversed, Record.ESTIMATION_METHODS))[row['Estimation_method']],
            estimation_method_detailed = dict(map(reversed, Record.ESTIMATION_METHODS_DETAILED))[row['Estimation_method_detailed']],
            road = dict(map(reversed, Record.ROADS))[row['Road']],
            road_category = dict(map(reversed, Record.ROAD_CATEGORIES))[row['RoadCategory']],
            count_point_ref = row['CP'],
            easting = easting,
            latitude = coord_x,
            northing = northing,
            longitude = coord_y,
            junc_start = row['StartJunction'],
            junc_end = row['EndJunction'],
            len_net_km = row['LinkLength_km'],
            len_net_mi = row['LinkLength_miles'],
            # record_year = row['AADFYear'],
            # AllHGVs = row['AllHGVs'],
            # AllMotorVehicles = row['AllMotorVehicles'],
            # PedalCycles = row['PedalCycles'],
            # Motorcycles = row['Motorcycles'],
            # CarsTaxis = row['CarsTaxis'],
            # BusesCoaches = row['BusesCoaches'],
            # LightGoodsVehicles = row['LightGoodsVehicles'],
            # V2AxleRigidHGV = row['V2AxleRigidHGV'],
            # V3AxleRigidHGV = row['V3AxleRigidHGV'],
            # V4or5AxleRigidHGV = row['V4or5AxleRigidHGV'],
            # V3or4AxleArticHGV = row['V3or4AxleArticHGV'],
            # V5AxleArticHGV = row['V5AxleArticHGV'],
        )
        print(' | {} - {}'.format(s1, c))

        for cv, vehicle_type in enumerate(vehicle_types):
            vc, s2 = VehicleCount.objects.get_or_create(record=r,
                vehicle_type=dict(map(reversed, VehicleCount.VEHICLE_TYPES))[vehicle_type],
                count=row[vehicle_type])
            print(' - {} - {}'.format(s2, cv))


create_records()

# > get set(row[value])
# l = []
# for row in df.to_dict(orient='records'):
#     l.append( row['Road'] )
# print(set(l))


# > get max(len()) for each field
# l3 = []
# for h in df.head():
#   l3.append( {h: max([len(str(l)) for l in (set([x for x in df[h]]))]) } )
# print(l3)