#saltwater_intrusion1.py

import arcpy
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
	ss_boundary = 
	## Find areas that will be safe from SS and SLR

	## Find areas that will be affected by SS and SLR
	return([ss_zone, slr_zone])
