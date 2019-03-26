#saltwater_intrusion1.py

import arcpy
from arcpy.sa import *
from config import gdb, data_dir, tmp_dir, out_dir
arcpy.env.workspace = gdb

def saltwater_intrusion1(oahu_dem, oahu_land_area, ss_val, slr_val):
	'''Performs the first part of the salwater intrusion impact assessment.
	Parameters:
	oahu_dem - 
	oahu_land_area - 
	ss_val - 
	slr_val - 
	Returns:
	ss_zone - 
	slr_zone - 
	'''
	## Create contours for SS and SLR limits
	ss_boundary = tmp_dir + "ss_boundary.shp"
	ContourList(oahu_dem, ss_boundary, ss_val)
	slr_boundary = tmp_dir + "slr_boundary.shp"
	ContourList(oahu_dem, slr_boundary, slr_val)

	## Find areas that will be safe from SS and SLR
	ss_safe_zone = gdb + "ss_safe_zone"
	arcpy.FeatureToPolygon(ss_boundary, ss_safe_zone)
	slr_safe_zone = gdb + "slr_safe_zone"
	arcpy.FeatureToPolygon(slr_boundary, slr_safe_zone)

	## Find areas that will be affected by SS and SLR
	ss_zone = gdb + "ss_zone"
	arcpy.Erase_analysis(ss_safe_zone, slr_safe_zone, ss_zone)
	slr_zone = gdb + "slr_zone"
	arcpy.Erase_analysis(oahu_land_area, slr_safe_zone, slr_zone)

	return([ss_zone, slr_zone])
