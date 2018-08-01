# Script to merge the group layers

# ===========
pathName = "Z:\wgp_data\WGP_fire_mapping_lr_copy.mxd" # Path name to mxd
saveTo = "Z:\wgp_data\Vectors\Merges\\"  # Out path
# ==========

import arcpy

mxd = arcpy.mapping.MapDocument(pathName)  # Set the map document
layers = arcpy.mapping.ListLayers(mxd)  # List the layers
feature_layers = []  # Create a blank list for non-group layers to be appended into

for layer in layers:  # Loop through the layers
    # Group Layers "1988 to 1989" etc.
    if "to" in layer.name:
        if feature_layers != []: # When the feature layers list isn't blank
            arcpy.Merge_management(feature_layers, saveTo + str(group_layer) + "_merge")  # Perform the merge. Save as "1989_to_1990" etc.
        group_layer = layer.name # Reset the layer name for the next iteration
        feature_layers = []  #Empty the feature layers.
    else: # I.e. on first iteration, or a new group layer
        feature_layers.append(layer.name) # Add all the feature layers under the group layer.
        
                                   
        
