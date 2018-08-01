# Script to clip the files to the extent of the boundary
# =============
outFile = "E:\wgp_data\Vectors\Clipped\\" # Output Directory
mapPath = "E:\documentation\liam\mxds\yslb.mxd" # Path to mxd, and mxd name
clipPolygon = "Mainland_clip_mga51" # Polygon for everyhing to be clipped to
searchLayer = "yslb" # Term used to filter layers  to be clipped
clusterTolerance = "" # Set cluster tolerance [optional]
# ============

import arcpy

mxd = arcpy.mapping.MapDocument(mapPath)  # Set the map doc

layers = arcpy.mapping.ListLayers(mxd)  # List the layers in the map doc

for layer in layers:  # Loop through the layers
    if searchLayer in layer.name:  # When the layer name contains the search term
        arcpy.AddMessage("Clipping " + str(layer.name) + " to extent " + str(clipPolygon))  # Displays message - [file] clipped to [extent]
        #[0:12] removed '_dissolve' - change this if the input file is different.
        arcpy.Clip_analysis(layer, clipPolygon, str(outFile) + str(layer.name) + "_Clipped", clusterTolerance)  # Clip the layer to the boundary
        arcpy.AddMessage("Clipping Successful")
        

arcpy.AddMessage("No more files meet the search term.")
arcpy.AddMessage("End of Process.")
