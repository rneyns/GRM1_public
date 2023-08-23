# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:41:10 2020

@author: Robbe Neyns
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from osgeo import gdal

def plot_spectral_signature(df):
  """
  A function to plot the spectral signatures of different classes extracted from the multi-spectral images in QGIS.
  The dataframe should contain the bands as columns and the land cover classes as rows.
  """
  #plot the spectral signature for each class
  fig, ax = plt.subplots(figsize=(15, 8))

  #Manipulate the dataframe for plotting
  df_pivot = df.T
  number_bands = np.arange(len(df_pivot))
  df_pivot.index = number_bands

  sns.lineplot(data=df_pivot)
  
def to_GeoTIFF(out_name, clf, data, raster):
  """
  Function to convert the classified raster of our ROI to geotiff.
  The result will also be plotted when using this function.
  """
  classified_raster = clf.predict(data.values).reshape((raster.RasterYSize,
  raster.RasterXSize))
  
  driverTiff = gdal.GetDriverByName('GTiff') 
  clfds = driverTiff.Create(out_name, raster.RasterXSize, raster.RasterYSize, 1, gdal.GDT_Float32)
  clfds.SetGeoTransform(raster.GetGeoTransform())
  clfds.SetProjection(raster.GetProjection())
  clfds.GetRasterBand(1).SetNoDataValue(-9999.0)
  clfds.GetRasterBand(1).WriteArray(classified_raster)
  
  #visualise the result 
  band = clfds.GetRasterBand(1)
  arr = band.ReadAsArray()
  plt.imshow(arr)
