# Necessary imports for code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# This is the beginning of me making my class for the analysis calculations

class Analysis:

# First I have to initialize the object with csvfiledata, the calibration factor, the length of the sample, and the diameter of the sample
    def __init__(self, csvFileData, calibrationFactor, length, diameter):
        self.data = csvFileData
        self.calibrationFactor = calibrationFactor
        self.length = length
        self.diameter = diameter


# This function will calculate the area of the sample. It is done by using the input diameter
# The units for the area is inches squared
    def area(self):
        return ((math.pi)/4)*(self.diameter)**2


# This function will calculate the vertical strain, load, area, and stress of the sample
# It is done using the data from the CSV file, as well as the input paramters.
# They are also added to the dataframe so that it is all in one combined table.
# The units for vertical strain is unitless since it is a ratio of the deformation and the length of the sample.
# The units for the load is in pounds.
# The units for the area is inches squared.
# The units for the calculated stress is pounds per square inch.
    def add_properties(self):
        self.data['Verical Strain'] = self.data['Deformation (in)']/ self.length
        self.data['Load (lb)'] = self.data['Dial Reading'] * self.calibrationFactor
        self.data['Corrected Area (in2)'] = self.area() / (1 - self.data['Verical Strain'])
        self.data['Stress (lb/in2)'] = self.data['Load (lb)'] / self.data['Corrected Area (in2)']


# The following code will plot the stress versus vertical strain curve
# The x-axis is the vertical strain calculations
# The y-axis is the stress calculations
    def plot_stress_vertical_strain(self):
        x = self.data['Verical Strain']
        y = self.data['Stress (lb/in2)']
        plt.plot(x, y, color='blue')

        plt.title('Stress vs. Vertical Strain', fontweight='black', fontfamily='monospace')
        plt.xlabel('Vertical Strain')
        plt.ylabel('Stress (lb/in2)')
        plt.grid(ls='-')
        plt.show()


# This function identifies the maximum stress value which is known as the unconfined compression strength
# It is done by using the max function to located the largest value in the stress data column
    def get_peak_strength(self):
        unconfined_compression_strength = max(self.data['Stress (lb/in2)'])
# A unit conversion from lb/in^2 to lb/ft^2 is performed in order to have it in the correct units to compare it to the classifaction data for consistency identification.
        ucs_psf = unconfined_compression_strength * 144
        return ucs_psf


# Classify the consistency of the clay using the unconfined compression strength of the sample according to the standards
# The classification ranges are set using if statements
    def classify_clay(self):
        ucs_psf = self.get_peak_strength()
        if 0 <= ucs_psf < 500 :
            print("Consistency of Clay Sample: Very Soft")
        elif 500 <= ucs_psf < 1000 :
            print("Consistency of Clay Sample: Soft")
        elif 1000 <= ucs_psf < 2000 :
            print("Consistency of Clay Sample: Medium")
        elif 2000 <= ucs_psf < 4000 :
            print("Consistency of Clay Sample: Stiff")
        elif 4000 <= ucs_psf <= 8000 :
            print("Consistency of Clay Sample: Very Stiff")
        else:
            print("invalid")


 # This is the end of the class Analysis
