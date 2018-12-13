# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:00:07 2018

@author: 44790
"""

# Import the Earth Engine Python Package
import ee

# Initialize the Earth Engine object, using the authentication credentials.
ee.Initialize()

# Print the information for an image asset.
image = ee.Image('srtm90_v4')
print(image.getInfo())
      