# Script to dissolve all the merged layers

# =======
mapDoc = "E:\wgp_data\WGP_fire_mapping_lr_copy.mxd"  # Path to the mxd
searchLayer = "_merge" # Search term to be used for layer
saveTo = "E:\wgp_data\Vectors\Dissolves\\"  # Out folder
# ======

import arcpy

mxd = arcpy.mapping.MapDocument(mapDoc)  # Set the mxd
layers = arcpy.mapping.ListLayers(mxd)  # List the layers in the map doc

for layer in layers:  # Loop through the layers
    if searchLayer in layer.name:  # If the search term is anywhere in the layer name (i.e. _merge)
        arcpy.Dissolve_management(layer.name, saveTo + str(layer.name)[0:12]+ "_dissolve") # Perform the dissolve

    
