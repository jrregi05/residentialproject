import arcpy

arcpy.env.workspace = "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles"
defineCensus = arcpy.management.DefineProjection("tl_2020_40_bg.shp", 'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]')
schoolPoints = arcpy.management.FeatureToPoint("OK_schools.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\Final_Test\\Default.gdb\\OK_schools_Points.shp", "CENTROID")
defineSchools = arcpy.management.DefineProjection("OK_schools_Points.shp", 'PROJCS["NAD_1983_StatePlane_Oklahoma_North_FIPS_3501_Feet",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",1968500.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-98.0],PARAMETER["Standard_Parallel_1",35.56666666666667],PARAMETER["Standard_Parallel_2",36.76666666666667],PARAMETER["Latitude_Of_Origin",35.0],UNIT["Foot_US",0.3048006096012192]]')
newCol = arcpy.management.CalculateField("tl_2020_40_bg.shp", "incomeName", "!GEOID!", "PYTHON3", '', "DOUBLE", "NO_ENFORCE_DOMAINS")
attributeJoin = arcpy.management.JoinField("tl_2020_40_bg.shp", "incomeName", "median_income_bg.csv", "name", None)
nearDistance = arcpy.analysis.Near("tl_2020_40_bg.shp", "OK_schools_Points.shp", "5 Miles", "NO_LOCATION", "NO_ANGLE", "PLANAR", "NEAR_FID NEAR_FID;NEAR_DIST NEAR_DIST;NEAR_FC Name")
schoolsToCensus = arcpy.analysis.SpatialJoin("tl_2020_40_bg.shp", "OK_schools_Points.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\Final_Test\\Default.gdb\\census_bg_schools.shp", "JOIN_ONE_TO_MANY", "KEEP_COMMON", 'STATEFP "STATEFP" true true false 2 Text 0 0,First,#,tl_2020_40_bg,STATEFP,0,2;COUNTYFP "COUNTYFP" true true false 3 Text 0 0,First,#,tl_2020_40_bg,COUNTYFP,0,3;TRACTCE "TRACTCE" true true false 6 Text 0 0,First,#,tl_2020_40_bg,TRACTCE,0,6;BLKGRPCE "BLKGRPCE" true true false 1 Text 0 0,First,#,tl_2020_40_bg,BLKGRPCE,0,1;GEOID "GEOID" true true false 12 Text 0 0,First,#,tl_2020_40_bg,GEOID,0,12;NAMELSAD "NAMELSAD" true true false 13 Text 0 0,First,#,tl_2020_40_bg,NAMELSAD,0,13;MTFCC "MTFCC" true true false 5 Text 0 0,First,#,tl_2020_40_bg,MTFCC,0,5;FUNCSTAT "FUNCSTAT" true true false 1 Text 0 0,First,#,tl_2020_40_bg,FUNCSTAT,0,1;ALAND "ALAND" true true false 14 Double 0 14,First,#,tl_2020_40_bg,ALAND,-1,-1;AWATER "AWATER" true true false 14 Double 0 14,First,#,tl_2020_40_bg,AWATER,-1,-1;INTPTLAT "INTPTLAT" true true false 11 Text 0 0,First,#,tl_2020_40_bg,INTPTLAT,0,11;INTPTLON "INTPTLON" true true false 12 Text 0 0,First,#,tl_2020_40_bg,INTPTLON,0,12;incomeName "incomeName" true true false 19 Double 0 0,First,#,tl_2020_40_bg,incomeName,-1,-1;id "id" true true false 254 Text 0 0,First,#,tl_2020_40_bg,id,0,254;name "name" true true false 19 Double 0 0,First,#,tl_2020_40_bg,name,-1,-1;Geographic "Geographic" true true false 254 Text 0 0,First,#,tl_2020_40_bg,Geographic,0,254;median_inc "median_inc" true true false 254 Text 0 0,First,#,tl_2020_40_bg,median_inc,0,254;NEAR_FID "NEAR_FID" true true false 10 Long 0 10,First,#,tl_2020_40_bg,NEAR_FID,-1,-1;NEAR_DIST "NEAR_DIST" true true false 19 Double 0 0,First,#,tl_2020_40_bg,NEAR_DIST,-1,-1;Object_ID "Object_ID" true true false 255 Text 0 0,First,#,OK_schools_Points,Object_ID,0,255;School_Nam "School_Nam" true true false 255 Text 0 0,First,#,OK_schools_Points,School_Nam,0,255;ORIG_FID "ORIG_FID" true true false 4 Long 0 0,First,#,OK_schools_Points,ORIG_FID,-1,-1;ObjID_Long "ObjID_Long" true true false 4 Long 0 0,First,#,OK_schools_Points,ObjID_Long,-1,-1', "WITHIN_A_DISTANCE", "5 Miles", '')


areaName = "Geographic"
incomeReq = "median_inc"
distFrSchool = "NEAR_DIST"
schoolinArea = "School_Nam"


def findPrivPub(privPub):
    for priv in privPub:
        if priv == "Private" or priv == "private":
            arcpy.Select_analysis("census_bg_schools.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\Schools_Selection.shp", '"{0}" NOT LIKE \'%ES%\' AND "{0}" NOT LIKE \'%MS%\' AND "{0}" NOT LIKE \'%HS%\''.format(schoolinArea))
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\Area_Selection.shp", '"{0}" <= \'{1}\''.format(incomeReq, userinputforincome))
        else:
            arcpy.Select_analysis("census_bg_schools.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\Schools_Selection.shp", '"{0}" LIKE \'%ES%\' OR "{0}" LIKE \'%MS%\' OR "{0}" LIKE \'%HS%\''.format(schoolinArea))
            


def findSchools(kidsAges):
    oldestElem = 11
    oldestMiddle = 13
    oldestHigh = 18
    needsElem = False
    needsMiddle = False
    needsHigh = False
    for kid in kidsAges:
        if kid < oldestElem:
            needsElem = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%ES%\''.format(schoolinArea))
        elif kid < oldestMiddle:
            needsMiddle = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%MS%\''.format(schoolinArea))
        elif kid < oldestHigh:
            needsHigh = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%HS%\''.format(schoolinArea))
        elif kid < oldestElem and kid < oldestMiddle:
            needsElem = True; needsMiddle = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%ES%\' OR "{0}" LIKE \'%MS%\''.format(schoolinArea))
        elif kid < oldestElem and kid < oldestHigh:
            needsElem = True; needsHigh = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%ES%\' OR "{0}" LIKE \'%HS%\''.format(schoolinArea))
        elif kid < oldestMiddle and kid < oldestHigh:
            needsMiddle = True; needsHigh = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%MS%\' OR "{0}" LIKE \'%HS%\''.format(schoolinArea))
        elif kid < oldestElem and kid < oldestMiddle and kid < oldestHigh:
            needsElem = True; needsMiddle = True; needsHigh = True
            arcpy.Select_analysis("Schools_Selection.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\PubSchoolSel.shp", '"{0}" LIKE \'%ES%\' OR "{0}" LIKE \'%MS%\' OR "{0}" LIKE \'%HS%\''.format(schoolinArea))


def bgIncome(householdIncome):
    arcpy.Select_analysis("PubSchoolSel.shp", "D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\Area_Selection.shp", '"{0}" <= \'{1}\''.format(incomeReq, userinputforincome))


def finalOutput():
    rows = arcpy.SearchCursor("D:\\OU\\Summer2022\\SpatialProgramming\\Term Project\\Final_Test_Shapefiles\\Area_Selection.shp", fields = "Geographic; median_inc; NEAR_DIST; School_Nam")
    for row in rows:
        print("Geographic area: {0}, Median Income: {1}, Distance, in miles, from school: {2}, School Name: {3}".format(
            row.getValue("Geographic"),
            row.getValue("median_inc"),
            row.getValue("NEAR_DIST"),
            row.getValue("School_Nam")))
    del cursor
