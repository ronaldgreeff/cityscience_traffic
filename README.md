# cityscience_traffic

A (Django) RESTful API providing traffic counts for Devon, South West.


# BUILD
Python==3.7
Django==2.2
djangorestframework==3.9.2


# SETTING UP LOCALLY
1. Edit environment details env.ps1 / env.sh as appropriate
2. Start the virtualenv with:

  > Bash
  python3 -m venv venv
  source venv/bin/activate
  source ./env.sh

  > PowerShell
  py -3 -m venv venv
  venv\scripts\activate
  .\env.ps1

3. Install requirements (pip install -r requirements.txt)
4. Setup postgres database
5. Run 'django makemigrations'
6. Run 'django migrate'
7. Run 'django createsuperuser'
8. Import Devon.csv data into database by running 'python import_csv.py'
9. Run 'python manage.py runserver' and check that the data succesfully imported by visiting http://127.0.0.1:8000


# DEMO
https://citysci-traffic.azurewebsites.net


# HOW TO USE
The API root (127.0.0.1:8000, or the demo link above) offers two means of accessing data:

"records" - Provides traffic counts per record (a record defined by location and time), with record-level filtering (year, estimation method, detailed estimation method, road and road category), and vehicle counts as a nested list.

"vehiclecounts" - Provides a traffic counts per vehicle type, with granular filtering on both record and vehicle type.

After selecting you access root, you can either use the "filter" button in the top right or query parameters to filter the data. For example, this query:

http://citysci-traffic.azurewebsites.net/records/?year=2000&estimation_method=0&estimation_method_detailed=0&road=0

Would filter records by:
    Year: 2000
    Estimation Method: Counted
    Estimation Method Detailed: Manual Count
    Road: A381

For more granular filtering, use http://citysci-traffic.azurewebsites.net/vehiclecounts/

An API mapping reference for URL parameters is provided below.


#CUSTOMISATION

1. FILTERING criteria can be customised by adding/removing fields from "filterset_fields" from either of the views specified in the views.py file.

2. DATA (fields and values) returned can be customised by adding/removing fields under 'class Meta' for each of the serializers specified in the serializers.py file.


# API MAPPING REFERENCE (FOR URL PARAMETERS):

    estimation_method:
        0: COUNTED
        1: ESTIMATED

    estimation_method_detailed:
        0: MANAUL_COUNT
        1: AUTOMATIC_COUNTER
        2: ESTIMATED_WITH_PREV
        3: ESTIMATED_FROM_NEAR
        4: NEIGHBOUR_DEPENDANT

    road:
        0: A381
        1: A386
        2: A3125
        3: A3052
        4: A3123
        5: A375
        6: A39
        7: A361
        8: A382
        9: M5
        10: A3126
        11: A384
        12: A30
        113: A380
        14: A388
        15: A383
        16: A303
        17: A3072
        18: A3121
        19: A35
        20: A373
        21: A3122
        22: A38
        23: A3079
        24: A379
        25: A376
        26: A377
        27: A390
        28: A3124
        29: A3015
        30: A399
        31: A396
        32: A385
        33: A358

    road_category:
        0: TA
        1: PA
        2: TM

    vehicle_type:
        0: ALLHGVS
        1: ALLMOTORVEHICLES
        2: PEDALCYCLES
        3: MOTORCYCLES
        4: CARSTAXIS
        5: BUSESCOACHES
        6: LIGHTGOODSVEHICLES
        7: V2AXLERIGIDHGV
        8: V3AXLERIGIDHGV
        9: V4OR5AXLERIGIDHGV
        10: V3OR4AXLEARTICHGV
        11: V5AXLEARTICHGV
        12: V6ORMOREAXLEARTICHGV