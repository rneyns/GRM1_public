# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:41:10 2020

@author: Robbe Neyns
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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