# Script to sample the DEM values at each point.

# ==========
inputRaster = "WGP_SPOT_COASTAL_DEM_mga51.tif" # DEM
outPath = "E:\wgp_data\Year_by_Year\DEM_Samples\\" # Out File & Path
resamplingTechnique = "NEAREST"
uniqueID = "FID"
slice = "CURRENT_SLICE"

# ==========
import arcpy

layers = arcpy.mapping.ListLayers(arcpy.mapping.MapDocument("CURRENT")) # Get the layers in the mxd
for layer in layers: # Loop through layers 
    try:
        int(layer.name) # Point files are years '2003', '2004' etc.
        arcpy.gp.Sample_sa(inputRaster, layer, outPath + str(layer.name) + "_DEM_Sampled", resamplingTechnique, str(layer.name) + "." + uniqueID, slice)  # Sample based on parameters set
        
    except ValueError: # Won't be able to convert the other layer names to int
        pass
    
