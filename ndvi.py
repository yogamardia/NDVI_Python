from osgeo import gdal
from gdalconst import *
from pyproj import Proj
from gdal import GetDriverByName
import numpy
from numpy import nan_to_num, add, subtract, divide, multiply
import math
import os


class NDVI:
    TAG = "NDVI.class"
    ds_B4 = None
    ds_B5 = None
    ndvi = None
    listener = None
    isCropped = False
    metadataPath = None
    cols = 0
    rows = 0
    output_cols = 0
    output_rows = 0

    lonStartCrop = 0
    latStartCrop = 0
    lonEndCrop = 0
    latEndCrop = 0

    def __init__(self):
        print ("NDVI instance created")

    def OpenB4File(self, path):
        print (self.TAG, "Band 4 path:", path)
        self.ds_B4 = gdal.Open(path, GA_ReadOnly)
        self.isCropped = False

    def OpenB5File(self, path):
        print (self.TAG, "Band 5 path:", path)
        self.ds_B5 = gdal.Open(path, GA_ReadOnly)
        self.isCropped = False

    def ReadMetadata(self, Meta):
        file = open(Meta, 'r')
        output = {}
        for line in file.readlines():
            if "=" in line:
                l = line.split("=")
                output[l[0].strip()] = l[1].strip()

        if not len(output) > 0:
            output = None

        return output 

    def SetCropCoordinate(self, latStart, latEnd, lonStart, lonEnd):
        self.latStartCrop = latStart
        self.latEndCrop = latEnd
        self.lonStartCrop = lonStart
        self.lonEndCrop = lonEnd

        print ("latStart: ", self.latStartCrop)
        print ("latEnd: ", self.latEndCrop)
        print ("lonStart: ", self.lonStartCrop)
        print ("lonEnd: ", self.lonEndCrop)

    def CropImage(self):
        self.cols = self.ds_B4.RasterXSize
        self.rows = self.ds_B4.RasterYSize
        bands = self.ds_B4.RasterCount
        print ("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)

        gt = self.ds_B4.GetGeoTransform()
        print ("GeoTransform: ", gt)
        x0 = gt[0]
        y0 = gt[3]
        pwidth = gt[1]
        pheight = gt[5]
        x_end = self.cols * pwidth + x0
        y_end = self.cols * pheight + y0

        myProj = Proj("+proj=utm +zone=50, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        lon, lat = myProj(x0, y0, inverse=True)
        x_utm, y_utm = myProj(lon, lat)
        print ("lon: ", lon, "\nlat: ", lat)
        print ("x_utm", x_utm, "\ny_utm", y_utm)

        x_mulai_crop_utm, y_mulai_crop_utm = myProj(self.lonStartCrop, self.latStartCrop)
        x_akhir_crop_utm, y_akhir_crop_utm = myProj(self.lonEndCrop, self.latEndCrop)
        print ("x_mulai_crop_utm: ", x_mulai_crop_utm, "\ny_mulai_crop_utm: ", y_mulai_crop_utm, "\nx_akhir_crop_utm: ", x_akhir_crop_utm, "\nx_akhir_crop_utm: ", y_akhir_crop_utm)

        xoff = int((x_mulai_crop_utm - x0) / pwidth)
        yoff = int((y_mulai_crop_utm -y0) / pheight)
        print ("xoff: ", xoff, "\nyoff: ", yoff)

        self.output_cols = int((x_akhir_crop_utm - x_mulai_crop_utm) / pwidth)
        self.output_rows = int((y_akhir_crop_utm - y_mulai_crop_utm) / pheight)

        band_B4 = self.ds_B4.GetRasterBand(1)
        band_B5 = self.ds_B5.GetRasterBand(1)

        self.data_B4 = band_B4.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)
        self.data_B5 = band_B5.ReadAsArray(xoff, yoff, self.output_cols, self.output_rows)

        print ("\nData Band 4: \n", self.data_B4, "\n")
        print ("Data Band 5: \n", self.data_B5, "\n")

        self.isCropped = True

        if (self.listener != None):
            self.listener.onCropFinish(self.data_B4, self.data_B5)

    def setupFullImage(self):
        self.cols = self.ds_B4.RasterXSize
        self.rows = self.ds_B4.RasterYSize
        bands = self.ds_B4.RasterCount
        print ("cols: ", self.cols, "\nrows: ", self.rows, "\nbands: ", bands)

        self.output_cols = self.cols
        self.output_rows = self.rows

        band_B4 = self.ds_B4.GetRasterBand(1)
        band_B5 = self.ds_B5.GetRasterBand(1)

        self.data_B4 = band_B4.ReadAsArray(0, 0, self.output_cols, self.output_rows)
        self.data_B5 = band_B5.ReadAsArray(0, 0, self.output_cols, self.output_rows)

    def StartCorrection(self):
        self.metadata = open(self.metadataPath, 'r')
        metadata = self.buildMetaData(self.metadata)
        B4_multi = float(metadata['REFLECTANCE_MULT_BAND_4'])
        B4_add = float(metadata['REFLECTANCE_ADD_BAND_4'])
        B5_multi = float(metadata['REFLECTANCE_MULT_BAND_5'])
        B5_add = float(metadata['REFLECTANCE_ADD_BAND_5'])
        sun_elevation = float(metadata['SUN_ELEVATION'])

        print ("MTL: ", B4_multi, B4_add, B5_multi, B5_add, sun_elevation)

        dataB4_ref = (self.data_B4 * B4_multi) + B4_add
        dataB5_ref = (self.data_B5 * B5_multi) + B5_add

        self.data_B4 = dataB4_ref / math.sin(sun_elevation)
        self.data_B5 = dataB5_ref / math.sin(sun_elevation)
        print ("Correct:", self.data_B4, self.data_B5)

    def StartNDVI(self):
        if not self.isCropped:
            self.setupFullImage()

        if self.metadataPath is not None:
            self.StartCorrection()

        data_B4_32 = self.data_B4.astype(numpy.float32)
        data_B5_32 = self.data_B5.astype(numpy.float32)

        numerator = subtract(data_B5_32, data_B4_32)
        denominator = add(data_B5_32, data_B4_32)
        self.ndvi = divide(numerator, denominator)

        print ("NDVI: \n", self.ndvi, "\n")

        if (self.listener != None):
            self.listener.onNDVIFinish(self.ndvi)
            # self.saveResult()

    def setMetaData(self, path):
        self.metadataPath = path

    def buildMetaData(self, file):
        output = {} #Dict
        for line in file.readlines():
            if "=" in line:
                l = line.split("=")
                output[l[0].strip()] = l[1].strip()
        return output

    def SetOnProcessFinishListener(self, listener):
        self.listener = listener


    def SaveResult(self, path):
        geotiff = GetDriverByName('Gtiff')
        output = geotiff.Create(path, self.output_cols, self.output_rows, 1, gdal.GDT_Float32)
        output_band = output.GetRasterBand(1)
        output_band.WriteArray(self.ndvi)
        output.SetGeoTransform(self.ds_B4.GetGeoTransform())
        print ("File created successfully.")

class OnProcessFinishListener:
    def onNDVIFinish(self, result):
        print ("ndvi finished")

    def onCropFinish(self, red, nir):
        print ("crop finished")





