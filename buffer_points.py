# Script to buffer the points so they have a 90 metre diameter.
import arcpy
# ===================
# To be used in the Python Window in ArcMap
outFolder = "E:\wgp_data\Year_by_Year\Buffered_Sampled_Points\\" # Out Path
bufferDist = 45   # Uses map units
# ===================

layers = arcpy.mapping.ListLayers(arcpy.mapping.MapDocument("CURRENT")) # List all the layers in the mxd
for layer in layers: # Loop through the layers
    outPath = outFolder + str(layer.name) + "_buffered" # Create the file name
    arcpy.Buffer_analysis(layer, outPath, bufferDist) # Perform the buffer
