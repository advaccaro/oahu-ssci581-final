#preprocessing.py
'''Performs all preprocessing necessary for the remainder of the script'''

import arcpy
from config import gdb, data_dir, tmp_dir, out_dir
arcpy.env.workspace = gdb
