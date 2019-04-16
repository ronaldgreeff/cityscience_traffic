GLOBAL_FILTERS = ()
RECORD_FILTERS = ('year', 'estimation_method', 'estimation_method_detailed', 'road', 'road_category',) + GLOBAL_FILTERS
VEHICLE_COUNT_FILTERS = ('vehicle_type', 'record__year', 'record__estimation_method', 'record__estimation_method_detailed', 'record__road', 'record__road_category') + GLOBAL_FILTERS
GLOBAL_EXCLUDES = ('id',)
RECORD_EXCLUDES = ('northing', 'easting', 'year', 'record_year', 'estimation_method', 'estimation_method_detailed', 'road_category') + GLOBAL_EXCLUDES
VEHICLE_COUNT_EXCLUDES = ('record',) + GLOBAL_EXCLUDES
ALL_FIELDS = ('year', 'estimation_method', 'estimation_method_detailed', 'road', 'road_category', 'id', 'easting', 'northing', 'latitude', 'longitude', 'AllHGVs', 'AllMotorVehicles', 'PedalCycles', 'Motorcycles', 'CarsTaxis', 'BusesCoaches', 'LightGoodsVehicles', 'V2AxleRigidHGV', 'V3AxleRigidHGV', 'V4or5AxleRigidHGV', 'V3or4AxleArticHGV', 'V5AxleArticHGV', 'junc_start', 'junc_end', 'len_net_km', 'len_net_mi', 'count_point_ref', 'record', 'vehicle_type', 'count',)
ALL_USED = GLOBAL_EXCLUDES+GLOBAL_FILTERS+RECORD_EXCLUDES+RECORD_FILTERS+VEHICLE_COUNT_EXCLUDES+VEHICLE_COUNT_FILTERS

x = (field for field in ALL_FIELDS if field not in ALL_USED)

for i in x:
    print(i)