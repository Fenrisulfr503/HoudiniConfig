node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

import numpy as np

# location SRTM file
_file = "C:/Users/Administrator/Desktop/I47/I47/N35E096.hgt"

SAMPLES = 1201  # Change this to 3601 for SRTM1
with open(_file, 'rb') as hgt_data:
    elevations = np.fromfile(hgt_data, np.dtype('>i2'), SAMPLES * SAMPLES) \
        .reshape((SAMPLES, SAMPLES))

# Write to Houdini Geometry
"""

for row in range(SAMPLES):
    for current_index in range(SAMPLES):
        pt_index = current_index + row * SAMPLES
        val = elevations[row, current_index]
        
        pt = geo.point(pt_index)
        pos = pt.position()
        pt.setPosition((pos.x(), float(val), pos.z()))

"""
