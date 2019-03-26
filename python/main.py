#main.py
'''Driver script for the project.  Parses inputs and runs entire workflow.'''

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir
arcpy.env.workspace = gdb
import preprocessing as PRE
import saltwater_intrusion1 as SI1
import saltwater_intrusion2 as SI2
import saltwater_intrusion3 as SI3
import site_suitability as SSA

def main(hgrrc_all_wells, 
	nhd_point, 
	doh_aquifers,
	hawaii_lulc,
	oahu_dem,
	ss_val,
	slr_val):
	# Parse inputs

	# Preprocessing
	try:
		[
		good_wells, 
		good_aquifers, 
		used_good_aquifers, 
		good lulc, 
		oahu_land_area, 
		coastline
		] = PRE.preprocessing(
			hgrrc_all_wells, 
			nhd_point, 
			doh_aquifers, 
			hawaii_lulc, 
			oahu_dem
			)
	except Exception as e:
		print("Failure in preprocessing stage.")
		print(e)
		exit(1)

	# Saltwater intrusion assessment (part 1)
	try:
		[
		ss_zone, 
		slr_zone
		] = SI1.saltwater_intrusion1(
			oahu_dem,
			oahu_land_area,
			slr_val,
			ss_val
			)
	except Exception as e:
		print("Failure in saltwater intrusion assessment (part 1).")
		print(e)
		exit(2)

	# Saltwater intrusion assessment (part 2)
	try:
		[
		affected_aquifers, 
		unaffected_aquifers, 
		aquifer_stats
		] = SI2.saltwater_intrusion2(
			good_aquifers, 
			slr_zone, 
			ss_zone
			)
	except Exception as e:
		print("Failure in saltwater intrusion assessment (part 2).")
		print(e)
		exit(3)

	# Saltwater intrusion assessment (part 3)
	try:
		[
		unaffected_used_wells, 
		vulnerable_used_wells, 
		lost_used_wells, 
		compropised_used_wells
		] = SI3.saltwater_intrusion3(
			good_wells,
			used_good_aquifers,
			affected_aquifers,
			slr_zone,
			ss_zone
			)
	except Exception as e:
		print("Failure in saltwater intrusion assessment (part 3).")
		print(e)
		exit(4)

	# Site suitability analysis
	try:
		potential_well_sites = SSA.site_suitability(
			unaffected_aquifers,
			good_lulc,
			coastline,
			good_wells,
			affected_aquifers
			)
	except Exception as e:
		print("Failure in site suitability analysis.")
		print(e)
		exit(5)

	print("Workflow completed successfully.")
	exit(0)



