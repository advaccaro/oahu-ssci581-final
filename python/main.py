#main.py
'''Driver script for the project.  Parses inputs and runs entire workflow.'''

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir
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
	ss_vals,
	slr_vals):
	# Parse inputs

	# Preprocessing
	try:
		PRE.preprocessing()
	except Exception as e:
		print("Failure in preprocessing stage.")
		print(e)
		exit(1)

	# Saltwater intrusion assessment (part 1)
	try:
		SI1.saltwater_intrusion1()
	except Exception as e:
		print("Failure in saltwater intrusion assessment (part 1).")
		print(e)
		exit(2)

	# Saltwater intrusion assessment (part 2)
	try:
		SI2.saltwater_intrusion2()
	except Exception as e:
		print("Failure in saltwater intrusion assessment (part 2).")
		print(e)
		exit(3)

	# Saltwater intrusion assessment (part 3)
	try:
		SI3.saltwater_intrusion3()
	except Exception as e:
		print("Failure in saltwater intrusion assessment (part 3).")
		print(e)
		exit(4)

	# Site suitability analysis
	try:
		SSA.site_suitability()
	except Exception as e:
		print("Failure in site suitability analysis.")
		print(e)
		exit(5)

	print("Workflow completed successfully.")
	exit(0)



