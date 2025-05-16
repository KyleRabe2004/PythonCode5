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
ndvi_output_path = "ndvi_output_raster.tif"
smart_raster.save_raster(ndvi, ndvi_output_path)




# Part 2:
# Assign a variable to the parcels data shapefile path


#  Pass this to your new smart vector class


#  Calculate zonal statistics and add to the attribute table of the parcels shapefile

importlib.reload(l5)

vector_path = r"R:\2025\Spring\GEOG562\Students\rabeky\Lab5\Benton_County_TaxLots.shp"
smart_vector = l5.SmartVector(vector_path)
smart_vector.calculate_zonal_stats(ndvi_output_path)
smart_vector.save_vector("Benton_County_TaxLots_ndvi.shp")

#  Part 3: Optional
#  Use matplotlib to make a map of your census tracts with the average NDVI values


from kcr_lab5_functions import SmartVector
import matplotlib.pyplot as plt

# Initialize the SmartVector object with the shapefile path
vector_path = r"R:\2025\Spring\GEOG562\Students\rabeky\Lab5\Benton_County_TaxLots_ndvi.shp"
smart_vector = SmartVector(vector_path)

# Debugging: Check the GeoDataFrame
print(smart_vector.gdf.head())
print(smart_vector.gdf.columns)

# Plot the map
plt.style.use('ggplot')

fig, ax = plt.subplots(figsize=(10, 10))

smart_vector.gdf.plot(
    column="mean",
    ax=ax,
    legend=True,
    cmap="YlGn",
    edgecolor="black",
    linewidth=0.3,
    missing_kwds={
        "color": "lightgrey",
        "label": "Missing values"
    }
)

ax.set_title("Average NDVI by Taxlot", fontsize=16)
ax.axis("off")

plt.savefig("BentonCountyNDVI.png", dpi=300)
plt.show()