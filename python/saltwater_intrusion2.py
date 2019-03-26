#saltwater_intrusion2.py
'''Performs the second part of the salwater intrusion impact assessment.'''

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir
arcpy.env.workspace = gdb
