
#####################
# Block 1:  Import the packages you'll need
# 
# 

import os, sys
#import rasterio
import geopandas as gpd




##################
# Block 2: 
# set the working directory to the directory where the data are

# Change this to the directory where your data are

data_dir = r"R:\2025\Spring\GEOG562\Students\rabeky\Lab5"
os.chdir(data_dir)
print(os.getcwd())


##################
# Block 3: 
#   Set up a new smart raster class using rasterio  
#    that will have a method called "calculate_ndvi"

import os
import rasterio
import numpy as np

class SmartRaster:
    def __init__(self, raster_path):
        self.raster_path = raster_path
        self.metadata = self._extract_metadata()

    def _extract_metadata(self):
        with rasterio.open(self.raster_path) as src:
            bounds = src.bounds
            x_dim = src.width
            y_dim = src.height
            n_bands = src.count
            dtype = src.dtypes[0]

            return {
                "bounds": [[bounds.left, bounds.top], [bounds.right, bounds.bottom]],
                "x_dim": x_dim,
                "y_dim": y_dim,
                "n_bands": n_bands,
                "dtype": dtype
            }

    def calculate_ndvi(self, band4_index=4, band3_index=3):
        """Calculate NDVI using the NIR and Red bands."""
        with rasterio.open(self.raster_path) as src:
            # Read the NIR (band 4) and Red (band 3) bands
            nir = src.read(band4_index).astype('float32')
            red = src.read(band3_index).astype('float32')

            # Avoid division by zero
            ndvi = np.where((nir + red) == 0, 0, (nir - red) / (nir + red))

        return ndvi

    def save_raster(self, array, output_path, transform=None, crs=None):
        """Save a raster array to a file."""
        with rasterio.open(self.raster_path) as src:
            transform = transform or src.transform
            crs = crs or src.crs
            profile = src.profile

        # Update profile for the new raster
        profile.update(dtype=rasterio.float32, count=1, compress='lzw')

        with rasterio.open(output_path, 'w', **profile) as dst:
            dst.write(array, 1)










##################
# Block 4: 
#   Set up a new smart vector class using geopandas
#    that will have a method similar to what did in lab 4
#    to calculate the zonal statistics for a raster
#    and add them as a column to the attribute table of the vector