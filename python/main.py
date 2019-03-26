#main.py
'''Driver script for the project.  Parses inputs and runs entire workflow.'''

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir

def main(hgrrc_all_wells, 
	nhd_point, 
	doh_aquifers,
	hawaii_lulc,
	oahu_dem,
	ss_vals,
	slr_vals):
	# Parse inputs
