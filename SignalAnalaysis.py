# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
"""
Created onmain. May  8, 2018

@author: zemarchezi
"""
from scipy.signal import butter, lfilter
from scipy import interpolate as interp
import numpy as np
from spacepy import pycdf
import os
from waveletFunctions import wavelet, wave_signif

__author__  'zemarchezi'

#
#
##################################################################
# Functions used in the data manipulation and analysis
##################################################################
