#import os
#import kcr_lab5_functions as l5


# Lab 5 scripts


#  Part 1:

#  Assign a variable to the Landsat file 


# Pass this to your new smart raster class



# Calculate NDVI and save to and output file

import os
import importlib
import kcr_lab5_functions as l5

# Reload the module to ensure changes are reflected
importlib.reload(l5)

# Set the working directory
data_dir = r"R:\2025\Spring\GEOG562\Students\rabeky\Lab5"
os.chdir(data_dir)
print(os.getcwd())

# Assign a variable to the Landsat file
landsat_path = r"R:\2025\Spring\GEOG562\Students\rabeky\Lab5\Landsat_image_corv.tif"

# Pass this to your new SmartRaster class
smart_raster = l5.SmartRaster(landsat_path)

# Calculate NDVI and save to an output file
ndvi = smart_raster.calculate_ndvi()
ndvi_output_path = "ndvi_output_test1.tif"
smart_raster.save_raster(ndvi, ndvi_output_path)




# Part 2:
# Assign a variable to the parcels data shapefile path


#  Pass this to your new smart vector class


#  Calculate zonal statistics and add to the attribute table of the parcels shapefile



#  Part 3: Optional
#  Use matplotlib to make a map of your census tracts with the average NDVI values