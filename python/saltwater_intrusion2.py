#saltwater_intrusion2.py

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir
arcpy.env.workspace = gdb

def saltwater_intrusion2(good_aquifers, slr_zone, ss_zone):
	'''Performs the second part of the salwater intrusion impact assessment.
	Parameters:
	good_aquifers - 
	slr_zone - 
	ss_zone - 
	Returns: 
	affected_aquifers - 
	unaffected_aquifers - 
	aquifer_stats - 
	'''

	## Find aquifers affected by SS and SLR
	lost_aquifers = Clip(good_aquifers, slr_zone)
	vulnerable_aquifers = Clip(good_aquifers, ss_zone)

	## Join to good aquifers and calculate stats
	JoinFields(good_aquifers, lost_aquifers, vulnerable_aquifers)
	AddFields()
	good_aquifers0 = CalculateFields()
	aquifer_stats0 = SummaryStatistics()
	AddFields()
	aquifer_stats = CalculateFields()

	## Find affected and unaffected aquifers
	affected_aquifers = MakeFeatureLayer()
	unaffected_aquifers = MakeFeatureLayer()



	return([affected_aquifers, unaffected_aquifers, aquifer_stats])