import arcpy
from arcpy import env
dataFolder = env.workspace =  arcpy.GetParameterAsText(0) ##r'Z:\Python\FinalProject\FinalProject'
BusWeight = float(arcpy.GetParameterAsText(1))
SchoolWeight = float(arcpy.GetParameterAsText(2))
TrainWeight = float (arcpy.GetParameterAsText(3))
ParkWeight = float (arcpy.GetParameterAsText(4))
FoodWeight = float (arcpy.GetParameterAsText(5))
HealthWeight = float (arcpy.GetParameterAsText(6))
AccessDistance = arcpy.GetParameterAsText(7)
env.overwriteOutput = True

# Get extent of the feature class


# ##todo: create layers where only denver is covered
allbus = 'TRANS_RTDBUSTOPS_P.shp'
denver = 'ADMN_NEIGHBORHOOD_A.shp'
desc = arcpy.Describe(denver)
spatial_ref = desc.spatialReference
# Set environment coordinate system
arcpy.env.outputCoordinateSystem = spatial_ref
extent = desc.extent
# Set environment extent
arcpy.env.extent = extent
arcpy.env.cellSize = 500 ##feet
busstops=arcpy.management.SelectLayerByLocation(allbus,'INTERSECT',denver)
arcpy.management.CopyFeatures(busstops,'denverbus.shp')
#arcpy.management.MakeFeatureLayer(busstops,'denverbus.shp')
#print(f"Temporary layer 'denverbus' created from selection.")
health= 'CDPHE_Health_Facilities.shp'
healthpts=arcpy.management.SelectLayerByLocation(health,'INTERSECT',denver)
arcpy.management.CopyFeatures(healthpts,'denverhealthpts.shp')
schools = 'EDU_PUBLICSCHOOLS_P.shp'
school=arcpy.management.SelectLayerByLocation(schools,'INTERSECT',denver)
arcpy.management.CopyFeatures(school,'denverplcschool.shp')
food = 'HLTH_FOODRETAILLOCATIONS_P.shp'
foodloc = arcpy.management.SelectLayerByLocation(food,'INTERSECT',denver)
arcpy.management.CopyFeatures(foodloc,'denverFoodRetail.shp')
park = 'PARK_PARKLAND_A.shp'
parks =arcpy.management.SelectLayerByLocation(park,'INTERSECT',denver)
arcpy.management.CopyFeatures(parks,'denverparks.shp')
lightrail = 'TRANS_RAILTRANSITSTATIONS_P.shp'
lightstops = arcpy.management.SelectLayerByLocation(lightrail,'INTERSECT',denver)
arcpy.management.CopyFeatures(lightstops,'denverlightstops.shp')
#todo: Spatial join of services to neighborhoods
arcpy.analysis.SpatialJoin(
    target_features="ADMN_NEIGHBORHOOD_A.shp",
    join_features="denverplcschool.shp denverplcschool_JoinCount;denverlightstops.shp denverlightstops_JoinCount;denverhealthpts.shp denverhealthpts_JoinCount;denverFoodRetail.shp denverFoodRetail_JoinCount;denverbus.shp denverbus_JoinCount;denverparks.shp denverparks_JoinCount",
    out_feature_class=r"NeighborhoodsServices.shp",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='NBHD_ID "NBHD_ID" true true false 5 Long 0 5,First,#,ADMN_NEIGHBORHOOD_A,NBHD_ID,-1,-1;NBHD_NAME "NBHD_NAME" true true false 50 Text 0 0,First,#,ADMN_NEIGHBORHOOD_A,NBHD_NAME,0,49;TYPOLOGY "TYPOLOGY" true true false 50 Text 0 0,First,#,ADMN_NEIGHBORHOOD_A,TYPOLOGY,0,32;NOTES "NOTES" true true false 254 Text 0 0,First,#,ADMN_NEIGHBORHOOD_A,NOTES,0,49;GLOBALID "GLOBALID" true true false 38 Text 0 0,First,#,ADMN_NEIGHBORHOOD_A,GLOBALID,0,37;SCHOOL_DIS "SCHOOL_DIS" true true false 33 Text 0 0,First,#,denverplcschool,SCHOOL_DIS,0,32;SCHOOL_NUM "SCHOOL_NUM" true true false 12 Text 0 0,First,#,denverplcschool,SCHOOL_NUM,0,11;SCHOOL_NAM "SCHOOL_NAM" true true false 50 Text 0 0,First,#,denverplcschool,SCHOOL_NAM,0,49;SCH_NAME_F "SCH_NAME_F" true true false 60 Text 0 0,First,#,denverplcschool,SCH_NAME_F,0,59;SCHOOL_TYP "SCHOOL_TYP" true true false 40 Text 0 0,First,#,denverplcschool,SCHOOL_TYP,0,39;SCHOOL_LEV "SCHOOL_LEV" true true false 20 Text 0 0,First,#,denverplcschool,SCHOOL_LEV,0,19;GRADE_LEVE "GRADE_LEVE" true true false 20 Text 0 0,First,#,denverplcschool,GRADE_LEVE,0,19;ADDRESS_LI "ADDRESS_LI" true true false 70 Text 0 0,First,#,denverplcschool,ADDRESS_LI,0,54;ADDRESS__1 "ADDRESS__1" true true false 70 Text 0 0,First,#,denverplcschool,ADDRESS__1,0,54;CITY "CITY" true true false 254 Text 0 0,First,#,denverplcschool,CITY,0,29;STATE "STATE" true true false 254 Text 0 0,First,#,denverplcschool,STATE,0,11;ZIP "ZIP" true true false 70 Text 0 0,First,#,denverplcschool,ZIP,0,11;WEBSITE "WEBSITE" true true false 99 Text 0 0,First,#,denverplcschool,WEBSITE,0,98;NOTES_1 "NOTES" true true false 100 Text 0 0,First,#,denverplcschool,NOTES,0,99;LAST_VERIF "LAST_VERIF" true true false 8 Date 0 0,First,#,denverplcschool,LAST_VERIF,-1,-1;ADDRESS_ID "ADDRESS_ID" true true false 5 Long 0 5,First,#,denverplcschool,ADDRESS_ID,-1,-1;GLOBALID_1 "GLOBALID" true true false 38 Text 0 0,First,#,denverplcschool,GLOBALID,0,37;STATION_NA "STATION_NA" true true false 50 Text 0 0,First,#,denverlightstops,STATION_NA,0,49;LINE_NAME "LINE_NAME" true true false 50 Text 0 0,First,#,denverlightstops,LINE_NAME,0,49;STATUS "STATUS" true true false 254 Text 0 0,First,#,denverlightstops,STATUS,0,32;RTD_PID "RTD_PID" true true false 5 Long 0 5,First,#,denverlightstops,RTD_PID,-1,-1;PARKING_SP "PARKING_SP" true true false 5 Long 0 5,First,#,denverlightstops,PARKING_SP,-1,-1;YEAR_OPEN "YEAR_OPEN" true true false 12 Text 0 0,First,#,denverlightstops,YEAR_OPEN,0,11;TYPOLOGY_1 "TYPOLOGY" true true false 50 Text 0 0,First,#,denverlightstops,TYPOLOGY,0,49;NOTES_12 "NOTES" true true false 55 Text 0 0,First,#,denverlightstops,NOTES,0,54;GLOBALID_2 "GLOBALID" true true false 38 Text 0 0,First,#,denverlightstops,GLOBALID,0,37;OBJECTID "OBJECTID" true true false 4 Short 0 4,First,#,denverhealthpts,OBJECTID,-1,-1;Facility_I "Facility_I" true true false 9 Text 0 0,First,#,denverhealthpts,Facility_I,0,8;Facility_N "Facility_N" true true false 87 Text 0 0,First,#,denverhealthpts,Facility_N,0,86;Facility_T "Facility_T" true true false 3 Text 0 0,First,#,denverhealthpts,Facility_T,0,2;Facility_1 "Facility_1" true true false 25 Text 0 0,First,#,denverhealthpts,Facility_1,0,24;Map_Symbol "Map_Symbol" true true false 37 Text 0 0,First,#,denverhealthpts,Map_Symbol,0,36;Facility_2 "Facility_2" true true false 40 Text 0 0,First,#,denverhealthpts,Facility_2,0,39;Facility_3 "Facility_3" true true false 8 Text 0 0,First,#,denverhealthpts,Facility_3,0,7;Licensed_B "Licensed_B" true true false 3 Short 0 3,First,#,denverhealthpts,Licensed_B,-1,-1;Telephone "Telephone" true true false 26 Text 0 0,First,#,denverhealthpts,Telephone,0,25;County "County" true true false 254 Text 0 0,First,#,denverhealthpts,County,0,10;Address_Fu "Address_Fu" true true false 254 Text 0 0,First,#,denverhealthpts,Address_Fu,0,81;Latitude "Latitude" true true false 19 Double 15 18,First,#,denverhealthpts,Latitude,-1,-1;Longitude "Longitude" true true false 19 Double 15 18,First,#,denverhealthpts,Longitude,-1,-1;CDPHE_HFEM "CDPHE_HFEM" true true false 14 Text 0 0,First,#,denverhealthpts,CDPHE_HFEM,0,13;Operating_ "Operating_" true true false 7 Text 0 0,First,#,denverhealthpts,Operating_,0,6;Trauma_Lev "Trauma_Lev" true true false 29 Text 0 0,First,#,denverhealthpts,Trauma_Lev,0,28;Date_Data_ "Date_Data_" true true false 8 Date 0 0,First,#,denverhealthpts,Date_Data_,-1,-1;Source "Source" true true false 63 Text 0 0,First,#,denverhealthpts,Source,0,62;NAME "NAME" true true false 254 Text 0 0,First,#,denverFoodRetail,NAME,0,253;ADDRESS__2 "ADDRESS_FU" true true false 254 Text 0 0,First,#,denverFoodRetail,ADDRESS_FU,0,253;ADDRESS "ADDRESS" true true false 254 Text 0 0,First,#,denverFoodRetail,ADDRESS,0,253;CITY_1 "CITY" true true false 254 Text 0 0,First,#,denverFoodRetail,CITY,0,253;STATE_1 "STATE" true true false 254 Text 0 0,First,#,denverFoodRetail,STATE,0,253;COUNTY_1 "COUNTY" true true false 254 Text 0 0,First,#,denverFoodRetail,COUNTY,0,253;ZIP_1 "ZIP" true true false 10 Long 0 10,First,#,denverFoodRetail,ZIP,-1,-1;LAT "LAT" true true false 19 Double 0 0,First,#,denverFoodRetail,LAT,-1,-1;LONG "LONG" true true false 19 Double 0 0,First,#,denverFoodRetail,LONG,-1,-1;TYPE "TYPE" true true false 254 Text 0 0,First,#,denverFoodRetail,TYPE,0,253;SNAP "SNAP" true true false 254 Text 0 0,First,#,denverFoodRetail,SNAP,0,253;DUFB "DUFB" true true false 254 Text 0 0,First,#,denverFoodRetail,DUFB,0,253;WIC "WIC" true true false 254 Text 0 0,First,#,denverFoodRetail,WIC,0,253;STATUS_1 "STATUS" true true false 254 Text 0 0,First,#,denverFoodRetail,STATUS,0,253;NOTES_1_13 "NOTES" true true false 254 Text 0 0,First,#,denverFoodRetail,NOTES,0,253;GlobalID_3 "GlobalID" true true false 38 Text 0 0,First,#,denverFoodRetail,GlobalID,0,37;BUS_STOPID "BUS_STOPID" true true false 19 Double 0 0,First,#,denverbus,BUS_STOPID,-1,-1;LONGITUD_1 "LONGITUDE" true true false 19 Double 0 0,First,#,denverbus,LONGITUDE,-1,-1;LATITUDE_1 "LATITUDE" true true false 19 Double 0 0,First,#,denverbus,LATITUDE,-1,-1;X_COORD "X_COORD" true true false 19 Double 0 0,First,#,denverbus,X_COORD,-1,-1;Y_COORD "Y_COORD" true true false 19 Double 0 0,First,#,denverbus,Y_COORD,-1,-1;ROUTES "ROUTES" true true false 254 Text 0 0,First,#,denverbus,ROUTES,0,253;STOP_NAME "STOP_NAME" true true false 254 Text 0 0,First,#,denverbus,STOP_NAME,0,253;DIRECTION "DIRECTION" true true false 254 Text 0 0,First,#,denverbus,DIRECTION,0,253;DISTANCE_F "DISTANCE_F" true true false 19 Double 0 0,First,#,denverbus,DISTANCE_F,-1,-1;POSTAL "POSTAL" true true false 5 Text 0 0,First,#,denverbus,POSTAL,0,4;PID "PID" true true false 10 Long 0 10,First,#,denverbus,PID,-1,-1;LOCATION "LOCATION" true true false 254 Text 0 0,First,#,denverbus,LOCATION,0,253;GLOBALID_4 "GLOBALID" true true false 38 Text 0 0,First,#,denverbus,GLOBALID,0,37;LOCATION_1 "LOCATION" true true false 254 Text 0 0,First,#,denverparks,LOCATION,0,253;FORMAL_NAM "FORMAL_NAM" true true false 254 Text 0 0,First,#,denverparks,FORMAL_NAM,0,253;LOC_CODE "LOC_CODE" true true false 254 Text 0 0,First,#,denverparks,LOC_CODE,0,253;PARK_TYPE "PARK_TYPE" true true false 254 Text 0 0,First,#,denverparks,PARK_TYPE,0,253;PARK_CLASS "PARK_CLASS" true true false 254 Text 0 0,First,#,denverparks,PARK_CLASS,0,253;GIS_ACRES "GIS_ACRES" true true false 19 Double 0 0,First,#,denverparks,GIS_ACRES,-1,-1;DESIGNATED "DESIGNATED" true true false 254 Text 0 0,First,#,denverparks,DESIGNATED,0,253;FIRST_AQ_D "FIRST_AQ_D" true true false 254 Text 0 0,First,#,denverparks,FIRST_AQ_D,0,253;MASTER_PLA "MASTER_PLA" true true false 254 Text 0 0,First,#,denverparks,MASTER_PLA,0,253;MAINT_DIST "MAINT_DIST" true true false 254 Text 0 0,First,#,denverparks,MAINT_DIST,0,253;COUNCIL_DI "COUNCIL_DI" true true false 254 Text 0 0,First,#,denverparks,COUNCIL_DI,0,253;POLICE_DIS "POLICE_DIS" true true false 254 Text 0 0,First,#,denverparks,POLICE_DIS,0,253;CROSS_STRE "CROSS_STRE" true true false 254 Text 0 0,First,#,denverparks,CROSS_STRE,0,253;ADDRESS__3 "ADDRESS_ID" true true false 19 Double 0 0,First,#,denverparks,ADDRESS_ID,-1,-1;ADDRESS__4 "ADDRESS_LI" true true false 70 Text 0 0,First,#,denverparks,ADDRESS_LI,0,69;ADDRESS__5 "ADDRESS__1" true true false 70 Text 0 0,First,#,denverparks,ADDRESS__1,0,69;CITY_12 "CITY" true true false 70 Text 0 0,First,#,denverparks,CITY,0,69;STATE_12 "STATE" true true false 30 Text 0 0,First,#,denverparks,STATE,0,29;ZIP_12 "ZIP" true true false 70 Text 0 0,First,#,denverparks,ZIP,0,69;LATITUDE_2 "LATITUDE" true true false 19 Double 0 0,First,#,denverparks,LATITUDE,-1,-1;LONGITUD_2 "LONGITUDE" true true false 19 Double 0 0,First,#,denverparks,LONGITUDE,-1,-1;MARKETING_ "MARKETING_" true true false 254 Text 0 0,First,#,denverparks,MARKETING_,0,253;FACILITIES "FACILITIES" true true false 254 Text 0 0,First,#,denverparks,FACILITIES,0,253;DIAGRAM "DIAGRAM" true true false 254 Text 0 0,First,#,denverparks,DIAGRAM,0,253;PHOTO "PHOTO" true true false 254 Text 0 0,First,#,denverparks,PHOTO,0,253;PARCEL_MAT "PARCEL_MAT" true true false 254 Text 0 0,First,#,denverparks,PARCEL_MAT,0,253;BND_QC "BND_QC" true true false 8 Date 0 0,First,#,denverparks,BND_QC,-1,-1;GLOBALID_5 "GLOBALID" true true false 38 Text 0 0,First,#,denverparks,GLOBALID,0,37',
    match_option="INTERSECT",
    search_radius=None,
    distance_field_name="",
    match_fields=None
)
#Todo: give weights to each service
fields = ['denverplcs','denverligh','denverheal','denverFood','denverbus_','denverpark']
cursor = arcpy.da.UpdateCursor('NeighborhoodsServices.shp',fields)
for row in cursor:
    school = row[0]
    light = row[1]
    health = row[2]
    food = row[3]
    bus = row[4]
    park = row[5]
    school = school * SchoolWeight# 3
    health = health * HealthWeight #5
    food = food * FoodWeight# 4
    park = park * ParkWeight#2
    bus = bus * BusWeight
    light = light * TrainWeight
    row[0] = school
    cursor.updateRow(row)
    row[2]=health
    cursor.updateRow(row)
    row[3]=food
    cursor.updateRow(row)
    row[5]=park
    cursor.updateRow(row)
    row[4]=bus
    cursor.updateRow(row)
    row[1]=light
    cursor.updateRow(row)
del cursor
score = arcpy.management.AddField('NeighborhoodsServices.shp','ServScore','LONG')
fields = ['denverplcs','denverligh','denverheal','denverFood','denverbus_','denverpark', 'ServScore']
cursor = arcpy.da.UpdateCursor('NeighborhoodsServices.shp',fields)
for row in cursor:
    school = row[0]
    light = row[1]
    health = row[2]
    food = row[3]
    bus = row[4]
    park = row[5]
    score = row[6]
    score = school + light + health +food +bus+park
    row[6] = score
    cursor.updateRow(row)
arcpy.GetMessages('Finished calculating raw services scores')
del cursor
bus = 'denverbus.shp'
food = 'denverFoodRetail.shp'
health = 'denverhealthpts.shp'
rail = 'denverlightstops.shp'
park = 'denverparks.shp'
school = 'denverplcschool.shp'
buffer_dis = AccessDistance 
busbuffer = arcpy.analysis.Buffer(bus, 'bufferbus.shp', buffer_dis, dissolve_option="ALL")
foodbuffer = arcpy.analysis.Buffer(food, 'bufferfood.shp', buffer_dis, dissolve_option="ALL")
healthbuffer = arcpy.analysis.Buffer(health, 'bufferhealth.shp', buffer_dis, dissolve_option="ALL")
railbuffer = arcpy.analysis.Buffer(rail, 'bufferrail.shp', buffer_dis, dissolve_option="ALL")
parkbuffer = arcpy.analysis.Buffer(park, 'bufferpark.shp', buffer_dis, dissolve_option="ALL")
schoolbuffer = arcpy.analysis.Buffer(school, 'bufferschool.shp', buffer_dis, dissolve_option="ALL")
#

arcpy.conversion.PolygonToRaster(busbuffer, 'ID', 'busbufferras.tif', cellsize =500)
arcpy.conversion.PolygonToRaster(foodbuffer, 'ID', 'foodbufferras.tif', cellsize =500)
arcpy.conversion.PolygonToRaster(healthbuffer, 'ID', 'healthbufferras.tif', cellsize =500)
arcpy.conversion.PolygonToRaster(railbuffer, 'ID', 'railbufferras.tif', cellsize =500)
arcpy.conversion.PolygonToRaster(parkbuffer, 'ID', 'parkbufferras.tif', cellsize =500)
arcpy.conversion.PolygonToRaster(schoolbuffer, 'ID', 'schoolbufferras.tif', cellsize =500)
# arcpy.conversion.PolygonToRaster('ADMN_NEIGHBORHOOD_A.shp', 'ID', 'denver.tif')
status = arcpy.CheckExtension('spatial')
if status:
    arcpy.CheckOutExtension('spatial')
    import arcpy.sa
    busraster = arcpy.Raster('busbufferras.tif')
    ## fill the Nodata to be 0
    # CON()
    busNull = arcpy.sa.IsNull(busraster)
    busraster_FILL = arcpy.sa.Con(busNull, 0, 1 )
    busraster_FILL.save("noweightedbus.tif")
    busraster_FILL = arcpy.sa.Int(busraster_FILL * BusWeight)
    busraster_FILL.save("weightedbus.tif") ##0, 7  -- bufffer
    foodraster = arcpy.Raster('foodbufferras.tif')
    foodNull = arcpy.sa.IsNull(foodraster)
    foodraster_FILL = arcpy.sa.Con(foodNull, 0, 1, )
    foodraster_FILL = arcpy.sa.Int(foodraster_FILL * FoodWeight)
    foodraster_FILL.save("weightedfood.tif")
    healthraster = arcpy.Raster('healthbufferras.tif')
    healthNull = arcpy.sa.IsNull(healthraster)
    healthraster_FILL = arcpy.sa.Con(healthNull, 0, 1, )
    healthraster_FILL = arcpy.sa.Int(healthraster_FILL * HealthWeight)
    healthraster_FILL.save("weightedhealth.tif")
    railraster = arcpy.Raster('railbufferras.tif')
    railNull = arcpy.sa.IsNull(railraster)
    railraster_FILL = arcpy.sa.Con(railNull, 0, 1, )
    railraster_FILL.save("noweightrail.tif")
    railraster_FILL = arcpy.sa.Int(railraster_FILL * TrainWeight)
    railraster_FILL.save("weightedrail.tif")
    parkraster = arcpy.Raster('parkbufferras.tif')
    parkNull = arcpy.sa.IsNull(parkraster)
    parkraster_FILL = arcpy.sa.Con(parkNull, 0, 1, )
    parkraster_FILL = arcpy.sa.Int(parkraster_FILL * ParkWeight)
    parkraster_FILL.save("weightedpark.tif")
    schoolraster = arcpy.Raster('schoolbufferras.tif')
    schoolNull = arcpy.sa.IsNull(schoolraster)
    schoolraster_FILL = arcpy.sa.Con(schoolNull, 0, 1, )
    schoolraster_FILL = arcpy.sa.Int(schoolraster_FILL * SchoolWeight)
    schoolraster_FILL.save("weightedschool.tif")
    otherScore = busraster_FILL + foodraster_FILL
    otherScore.save('otherScore.tif')
    scoreraster = healthraster_FILL + railraster_FILL  ##7/6
    scoreraster.save('other_scoreraster.tif')
    anotherscore = parkraster_FILL + schoolraster_FILL
    anotherscore.save('anotherscore.tif')
    finalscore = otherScore + scoreraster + anotherscore
    finalscore.save("final.tif")
    finalscore_reclass =arcpy.sa.SetNull((finalscore > 100) | (finalscore < -10), finalscore)
    finalscore_reclass.save("final_check.tif")
arcpy.CheckInExtension('spatial')
arcpy.conversion.RasterToPolygon(finalscore_reclass,'scorepoly.shp')
arcpy.analysis.SpatialJoin(
    target_features="NeighborhoodsServices.shp",
    join_features="scorepoly.shp Join_Count",
    out_feature_class=r"final.shp",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping='denverplcs "denverplcs" true true false 10 Long 0 0,First,#,NeighborhoodsServices,denverplcs,-1,-1;denverligh "denverligh" true true false 10 Long 0 0,First,#,NeighborhoodsServices,denverligh,-1,-1;denverheal "denverheal" true true false 10 Long 0 0,First,#,NeighborhoodsServices,denverheal,-1,-1;denverFood "denverFood" true true false 10 Long 0 0,First,#,NeighborhoodsServices,denverFood,-1,-1;denverbus_ "denverbus_" true true false 10 Long 0 0,First,#,NeighborhoodsServices,denverbus_,-1,-1;denverpark "denverpark" true true false 10 Long 0 0,First,#,NeighborhoodsServices,denverpark,-1,-1;TARGET_FID "TARGET_FID" true true false 10 Long 0 0,First,#,NeighborhoodsServices,TARGET_FID,-1,-1;NBHD_ID "NBHD_ID" true true false 5 Long 0 0,First,#,NeighborhoodsServices,NBHD_ID,-1,-1;NBHD_NAME "NBHD_NAME" true true false 50 Text 0 0,First,#,NeighborhoodsServices,NBHD_NAME,0,49;TYPOLOGY "TYPOLOGY" true true false 50 Text 0 0,First,#,NeighborhoodsServices,TYPOLOGY,0,49;NOTES "NOTES" true true false 254 Text 0 0,First,#,NeighborhoodsServices,NOTES,0,253;GLOBALID "GLOBALID" true true false 38 Text 0 0,First,#,NeighborhoodsServices,GLOBALID,0,37;SCHOOL_DIS "SCHOOL_DIS" true true false 33 Text 0 0,First,#,NeighborhoodsServices,SCHOOL_DIS,0,32;SCHOOL_NUM "SCHOOL_NUM" true true false 12 Text 0 0,First,#,NeighborhoodsServices,SCHOOL_NUM,0,11;SCHOOL_NAM "SCHOOL_NAM" true true false 50 Text 0 0,First,#,NeighborhoodsServices,SCHOOL_NAM,0,49;SCH_NAME_F "SCH_NAME_F" true true false 60 Text 0 0,First,#,NeighborhoodsServices,SCH_NAME_F,0,59;SCHOOL_TYP "SCHOOL_TYP" true true false 40 Text 0 0,First,#,NeighborhoodsServices,SCHOOL_TYP,0,39;SCHOOL_LEV "SCHOOL_LEV" true true false 20 Text 0 0,First,#,NeighborhoodsServices,SCHOOL_LEV,0,19;GRADE_LEVE "GRADE_LEVE" true true false 20 Text 0 0,First,#,NeighborhoodsServices,GRADE_LEVE,0,19;ADDRESS_LI "ADDRESS_LI" true true false 70 Text 0 0,First,#,NeighborhoodsServices,ADDRESS_LI,0,69;ADDRESS__1 "ADDRESS__1" true true false 70 Text 0 0,First,#,NeighborhoodsServices,ADDRESS__1,0,69;CITY "CITY" true true false 254 Text 0 0,First,#,NeighborhoodsServices,CITY,0,253;STATE "STATE" true true false 254 Text 0 0,First,#,NeighborhoodsServices,STATE,0,253;ZIP "ZIP" true true false 70 Text 0 0,First,#,NeighborhoodsServices,ZIP,0,69;WEBSITE "WEBSITE" true true false 99 Text 0 0,First,#,NeighborhoodsServices,WEBSITE,0,98;NOTES_1 "NOTES_1" true true false 100 Text 0 0,First,#,NeighborhoodsServices,NOTES_1,0,99;LAST_VERIF "LAST_VERIF" true true false 8 Date 0 0,First,#,NeighborhoodsServices,LAST_VERIF,-1,-1;ADDRESS_ID "ADDRESS_ID" true true false 5 Long 0 0,First,#,NeighborhoodsServices,ADDRESS_ID,-1,-1;GLOBALID_1 "GLOBALID_1" true true false 38 Text 0 0,First,#,NeighborhoodsServices,GLOBALID_1,0,37;STATION_NA "STATION_NA" true true false 50 Text 0 0,First,#,NeighborhoodsServices,STATION_NA,0,49;LINE_NAME "LINE_NAME" true true false 50 Text 0 0,First,#,NeighborhoodsServices,LINE_NAME,0,49;STATUS "STATUS" true true false 254 Text 0 0,First,#,NeighborhoodsServices,STATUS,0,253;RTD_PID "RTD_PID" true true false 5 Long 0 0,First,#,NeighborhoodsServices,RTD_PID,-1,-1;PARKING_SP "PARKING_SP" true true false 5 Long 0 0,First,#,NeighborhoodsServices,PARKING_SP,-1,-1;YEAR_OPEN "YEAR_OPEN" true true false 12 Text 0 0,First,#,NeighborhoodsServices,YEAR_OPEN,0,11;TYPOLOGY_1 "TYPOLOGY_1" true true false 50 Text 0 0,First,#,NeighborhoodsServices,TYPOLOGY_1,0,49;NOTES_12 "NOTES_12" true true false 55 Text 0 0,First,#,NeighborhoodsServices,NOTES_12,0,54;GLOBALID_2 "GLOBALID_2" true true false 38 Text 0 0,First,#,NeighborhoodsServices,GLOBALID_2,0,37;OBJECTID "OBJECTID" true true false 4 Short 0 0,First,#,NeighborhoodsServices,OBJECTID,-1,-1;Facility_I "Facility_I" true true false 9 Text 0 0,First,#,NeighborhoodsServices,Facility_I,0,8;Facility_N "Facility_N" true true false 87 Text 0 0,First,#,NeighborhoodsServices,Facility_N,0,86;Facility_T "Facility_T" true true false 3 Text 0 0,First,#,NeighborhoodsServices,Facility_T,0,2;Facility_1 "Facility_1" true true false 25 Text 0 0,First,#,NeighborhoodsServices,Facility_1,0,24;Map_Symbol "Map_Symbol" true true false 37 Text 0 0,First,#,NeighborhoodsServices,Map_Symbol,0,36;Facility_2 "Facility_2" true true false 40 Text 0 0,First,#,NeighborhoodsServices,Facility_2,0,39;Facility_3 "Facility_3" true true false 8 Text 0 0,First,#,NeighborhoodsServices,Facility_3,0,7;Licensed_B "Licensed_B" true true false 3 Short 0 0,First,#,NeighborhoodsServices,Licensed_B,-1,-1;Telephone "Telephone" true true false 26 Text 0 0,First,#,NeighborhoodsServices,Telephone,0,25;County "County" true true false 254 Text 0 0,First,#,NeighborhoodsServices,County,0,253;Address_Fu "Address_Fu" true true false 254 Text 0 0,First,#,NeighborhoodsServices,Address_Fu,0,253;Latitude "Latitude" true true false 19 Double 0 0,First,#,NeighborhoodsServices,Latitude,-1,-1;Longitude "Longitude" true true false 19 Double 0 0,First,#,NeighborhoodsServices,Longitude,-1,-1;CDPHE_HFEM "CDPHE_HFEM" true true false 14 Text 0 0,First,#,NeighborhoodsServices,CDPHE_HFEM,0,13;Operating_ "Operating_" true true false 7 Text 0 0,First,#,NeighborhoodsServices,Operating_,0,6;Trauma_Lev "Trauma_Lev" true true false 29 Text 0 0,First,#,NeighborhoodsServices,Trauma_Lev,0,28;Date_Data_ "Date_Data_" true true false 8 Date 0 0,First,#,NeighborhoodsServices,Date_Data_,-1,-1;Source "Source" true true false 63 Text 0 0,First,#,NeighborhoodsServices,Source,0,62;NAME "NAME" true true false 254 Text 0 0,First,#,NeighborhoodsServices,NAME,0,253;ADDRESS__2 "ADDRESS__2" true true false 254 Text 0 0,First,#,NeighborhoodsServices,ADDRESS__2,0,253;ADDRESS "ADDRESS" true true false 254 Text 0 0,First,#,NeighborhoodsServices,ADDRESS,0,253;CITY_1 "CITY_1" true true false 254 Text 0 0,First,#,NeighborhoodsServices,CITY_1,0,253;STATE_1 "STATE_1" true true false 254 Text 0 0,First,#,NeighborhoodsServices,STATE_1,0,253;COUNTY_1 "COUNTY_1" true true false 254 Text 0 0,First,#,NeighborhoodsServices,COUNTY_1,0,253;ZIP_1 "ZIP_1" true true false 10 Long 0 0,First,#,NeighborhoodsServices,ZIP_1,-1,-1;LAT "LAT" true true false 19 Double 0 0,First,#,NeighborhoodsServices,LAT,-1,-1;LONG "LONG" true true false 19 Double 0 0,First,#,NeighborhoodsServices,LONG,-1,-1;TYPE "TYPE" true true false 254 Text 0 0,First,#,NeighborhoodsServices,TYPE,0,253;SNAP "SNAP" true true false 254 Text 0 0,First,#,NeighborhoodsServices,SNAP,0,253;DUFB "DUFB" true true false 254 Text 0 0,First,#,NeighborhoodsServices,DUFB,0,253;WIC "WIC" true true false 254 Text 0 0,First,#,NeighborhoodsServices,WIC,0,253;STATUS_1 "STATUS_1" true true false 254 Text 0 0,First,#,NeighborhoodsServices,STATUS_1,0,253;NOTES_1_13 "NOTES_1_13" true true false 254 Text 0 0,First,#,NeighborhoodsServices,NOTES_1_13,0,253;GlobalID_3 "GlobalID_3" true true false 38 Text 0 0,First,#,NeighborhoodsServices,GlobalID_3,0,37;BUS_STOPID "BUS_STOPID" true true false 19 Double 0 0,First,#,NeighborhoodsServices,BUS_STOPID,-1,-1;LONGITUD_1 "LONGITUD_1" true true false 19 Double 0 0,First,#,NeighborhoodsServices,LONGITUD_1,-1,-1;LATITUDE_1 "LATITUDE_1" true true false 19 Double 0 0,First,#,NeighborhoodsServices,LATITUDE_1,-1,-1;X_COORD "X_COORD" true true false 19 Double 0 0,First,#,NeighborhoodsServices,X_COORD,-1,-1;Y_COORD "Y_COORD" true true false 19 Double 0 0,First,#,NeighborhoodsServices,Y_COORD,-1,-1;ROUTES "ROUTES" true true false 254 Text 0 0,First,#,NeighborhoodsServices,ROUTES,0,253;STOP_NAME "STOP_NAME" true true false 254 Text 0 0,First,#,NeighborhoodsServices,STOP_NAME,0,253;DIRECTION "DIRECTION" true true false 254 Text 0 0,First,#,NeighborhoodsServices,DIRECTION,0,253;DISTANCE_F "DISTANCE_F" true true false 19 Double 0 0,First,#,NeighborhoodsServices,DISTANCE_F,-1,-1;POSTAL "POSTAL" true true false 5 Text 0 0,First,#,NeighborhoodsServices,POSTAL,0,4;PID "PID" true true false 10 Long 0 0,First,#,NeighborhoodsServices,PID,-1,-1;LOCATION "LOCATION" true true false 254 Text 0 0,First,#,NeighborhoodsServices,LOCATION,0,253;GLOBALID_4 "GLOBALID_4" true true false 38 Text 0 0,First,#,NeighborhoodsServices,GLOBALID_4,0,37;LOCATION_1 "LOCATION_1" true true false 254 Text 0 0,First,#,NeighborhoodsServices,LOCATION_1,0,253;FORMAL_NAM "FORMAL_NAM" true true false 254 Text 0 0,First,#,NeighborhoodsServices,FORMAL_NAM,0,253;LOC_CODE "LOC_CODE" true true false 254 Text 0 0,First,#,NeighborhoodsServices,LOC_CODE,0,253;PARK_TYPE "PARK_TYPE" true true false 254 Text 0 0,First,#,NeighborhoodsServices,PARK_TYPE,0,253;PARK_CLASS "PARK_CLASS" true true false 254 Text 0 0,First,#,NeighborhoodsServices,PARK_CLASS,0,253;GIS_ACRES "GIS_ACRES" true true false 19 Double 0 0,First,#,NeighborhoodsServices,GIS_ACRES,-1,-1;DESIGNATED "DESIGNATED" true true false 254 Text 0 0,First,#,NeighborhoodsServices,DESIGNATED,0,253;FIRST_AQ_D "FIRST_AQ_D" true true false 254 Text 0 0,First,#,NeighborhoodsServices,FIRST_AQ_D,0,253;MASTER_PLA "MASTER_PLA" true true false 254 Text 0 0,First,#,NeighborhoodsServices,MASTER_PLA,0,253;MAINT_DIST "MAINT_DIST" true true false 254 Text 0 0,First,#,NeighborhoodsServices,MAINT_DIST,0,253;COUNCIL_DI "COUNCIL_DI" true true false 254 Text 0 0,First,#,NeighborhoodsServices,COUNCIL_DI,0,253;POLICE_DIS "POLICE_DIS" true true false 254 Text 0 0,First,#,NeighborhoodsServices,POLICE_DIS,0,253;CROSS_STRE "CROSS_STRE" true true false 254 Text 0 0,First,#,NeighborhoodsServices,CROSS_STRE,0,253;ADDRESS__3 "ADDRESS__3" true true false 19 Double 0 0,First,#,NeighborhoodsServices,ADDRESS__3,-1,-1;ADDRESS__4 "ADDRESS__4" true true false 70 Text 0 0,First,#,NeighborhoodsServices,ADDRESS__4,0,69;ADDRESS__5 "ADDRESS__5" true true false 70 Text 0 0,First,#,NeighborhoodsServices,ADDRESS__5,0,69;CITY_12 "CITY_12" true true false 70 Text 0 0,First,#,NeighborhoodsServices,CITY_12,0,69;STATE_12 "STATE_12" true true false 30 Text 0 0,First,#,NeighborhoodsServices,STATE_12,0,29;ZIP_12 "ZIP_12" true true false 70 Text 0 0,First,#,NeighborhoodsServices,ZIP_12,0,69;LATITUDE_2 "LATITUDE_2" true true false 19 Double 0 0,First,#,NeighborhoodsServices,LATITUDE_2,-1,-1;LONGITUD_2 "LONGITUD_2" true true false 19 Double 0 0,First,#,NeighborhoodsServices,LONGITUD_2,-1,-1;MARKETING_ "MARKETING_" true true false 254 Text 0 0,First,#,NeighborhoodsServices,MARKETING_,0,253;FACILITIES "FACILITIES" true true false 254 Text 0 0,First,#,NeighborhoodsServices,FACILITIES,0,253;DIAGRAM "DIAGRAM" true true false 254 Text 0 0,First,#,NeighborhoodsServices,DIAGRAM,0,253;PHOTO "PHOTO" true true false 254 Text 0 0,First,#,NeighborhoodsServices,PHOTO,0,253;PARCEL_MAT "PARCEL_MAT" true true false 254 Text 0 0,First,#,NeighborhoodsServices,PARCEL_MAT,0,253;BND_QC "BND_QC" true true false 8 Date 0 0,First,#,NeighborhoodsServices,BND_QC,-1,-1;GLOBALID_5 "GLOBALID_5" true true false 38 Text 0 0,First,#,NeighborhoodsServices,GLOBALID_5,0,37;ServScore "ServScore" true true false 10 Long 0 0,First,#,NeighborhoodsServices,ServScore,-1,-1;Id "Id" true true false 10 Long 0 0,First,#,scorepoly,Id,-1,-1;gridcode "gridcode" true true false 10 Long 0 0,Sum,#,scorepoly,gridcode,-1,-1',
    match_option="INTERSECT",
    search_radius=None,
    distance_field_name="",
    match_fields=None
)
