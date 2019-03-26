#site_suitability.py

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir
arcpy.env.workspace = gdb

def site_suitability(
	unaffected_aquifers,
	good_lulc,
	coastline,
	good_wells,
	affected_aquifers
	):
	'''Performs the water well site suitability analysis.
	Parameters:
	unaffected_aquifers - 
	good_lulc - 
	coastline - 
	good_wells - 
	affected_aquifers - 

	Returns:
	potential_well_sites - '''

	## Find unacceptable well areas
	# Create buffers
	coastline_buffer = gdb + "coastline_buffer"
	 arcpy.Buffer_analysis(
	 	coastline, 
	 	coastline_buffer,
	 	"1 km",
	 	"FULL",
	 	"ROUND",
	 	"ALL"
	 	)
	good_wells_buffer = gdb + "good_wells_buffer"
	arcpy.Buffer_analysis(
		good_wells, 
		good_wells_buffer, 
		"1 km",
		"FULL",
		"ROUND",
		"ALL"
		)
	affected_aquifers_buffer = gdb + "affected_aquifers_buffer"
	arcpy.Buffer_analysis(
		affected_aquifers, 
		affected_aquifers_buffer, 
		"2 km",
		"FULL",
		"ROUND",
		"ALL"
		)
	# Take the union of the buffers
	buffers_union = gdb + "buffers_union"
	arcpy.Union_analysis(
		[coastline_buffer, good_wells_buffer, affected_aquifers_buffer],
		buffers_union
		)

	## Find well sites that are in good LULC zones and unaffected aquifers
	arcpy.Intersect_analysis(
		[unaffected_aquifers, good_lulc], 
		ok_well_sites, 
		"ALL"
		)

	## Find potential well sites
	potential_well_sites = gdb + "potential_well_sites"
	arcpy.Erase_analysis(ok_well_sites, buffers_union, potential_well_sites)


	return(potential_well_sites)