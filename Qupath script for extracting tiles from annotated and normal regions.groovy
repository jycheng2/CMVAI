//size 300, 512 for centroid positive


/**
 * Script to export image tiles (can be customized in various ways).
 */
import groovy.time.TimeCategory 
import groovy.time.TimeDuration

Date start = new Date()

// Get the current image (supports 'Run for project')
def imageData = getCurrentImageData()

// Define output path (here, relative to project)
def name = GeneralTools.getNameWithoutExtension(imageData.getServer().getMetadata().getName())
def pathOutput = buildFilePath('d:/cmvt3', name, 'negative')
def pathOutput2 = buildFilePath('d:/cmvt3', name, 'positive_D')
def pathOutput3 = buildFilePath('d:/cmvt3', name, 'positive_CL')
def pathOutput4 = buildFilePath('d:/cmvt3', name, 'positive')
mkdirs(pathOutput)
mkdirs(pathOutput2)
mkdirs(pathOutput3)
mkdirs(pathOutput4)
// Define output resolution in calibrated units (e.g. µm if available)
//double requestedPixelSize = 10

// Convert output resolution to a downsample factor
double pixelSize = imageData.getServer().getPixelCalibration().getAveragedPixelSize()
//double downsample = requestedPixelSize / pixelSize

double downsample = 1
    
// Create an exporter that requests corresponding tiles from the original & labelled image servers
new TileExporter(imageData)
    .downsample(downsample)   // Define export resolution
    .imageExtension('.jpg')   // Define file extension for original pixels (often .tif, .jpg, '.png' or '.ome.tif')
    .tileSize(300)            // Define size of each tile, in pixels
    .annotatedTilesOnly(false) // If true, only export tiles if there is a (classified) annotation present
    .overlap(0)              // Define overlap, in pixel units at the export resolution
    .writeTiles(pathOutput)   // Write tiles to the specified directory
  
 // Create an exporter that requests corresponding tiles from the original & labelled image servers
new TileExporter(imageData)
    .downsample(downsample)   // Define export resolution
    .imageExtension('.jpg')   // Define file extension for original pixels (often .tif, .jpg, '.png' or '.ome.tif')
    .tileSize(300)            // Define size of each tile, in pixels
    .annotatedTilesOnly(true) // If true, only export tiles if there is a (classified) annotation present
    .overlap(0)              // Define overlap, in pixel units at the export resolution
    .writeTiles(pathOutput2)   // Write tiles to the specified directory
  

new TileExporter(imageData)
    .downsample(downsample)   // Define export resolution
    .imageExtension('.jpg')   // Define file extension for original pixels (often .tif, .jpg, '.png' or '.ome.tif')
    .tileSize(512)            // Define size of each tile, in pixels
    .annotatedTilesOnly(true) // If true, only export tiles if there is a (classified) annotation present
    .annotatedCentroidTilesOnly(true)
    .overlap(448)              // Define overlap, in pixel units at the export resolution
    .writeTiles(pathOutput3)   // Write tiles to the specified directory
  

print 'Done!'


//delete positive files


import groovy.io.FileType
import java.io.File;


String fn=""
dh = new File(pathOutput2)
dh.eachFile {
    fn=it.getName()
    File file = new File(pathOutput+"/"+fn)
    if( file.exists()){file.delete()
    println fn
    
    }
}


print "done"
Date stop = new Date()

TimeDuration td = TimeCategory.minus( stop, start )
print td
