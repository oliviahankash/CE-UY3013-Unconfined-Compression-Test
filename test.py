from source import Analysis

# Necessary imports for code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import interpolate

# Import your inital CSV data file
# This example is from the data table from my Input File
data = pd.read_csv('Unconfined_Compression_Test_InitialData.csv')
data


# This next set of code is so that the user can input their specific parameters for the calculations.
# This includes the calibration factor, the length of the sample, and the diameter of the sample.
# The input function will allow for easier calculations since everyone will have different parameters.
# The calibration factor pertains to one division of the proving ring on the unconfined compression testing machine. It is measured in pounds and can range anywhere from (0-1) pounds.
# The length of the sample is measured in inches.
# The diameter of the sample is measured in inches.
# A cylindrical soil specimen should have a height-to-diameter ratio of between 2 and 3.
calibrationFactor = float(input("Calibration Factor in lb: "))
length = float(input("Length in inches: "))
diameter = float(input("Diameter in inches: "))
print('\n')


# This is where the class is instantiated and the functions are called
# The outputs given are:
# - the area of the sample,
# - the Stress vs. Vertical Strain Curve
# - the Mohr Circle analysis with stress failures and undrained shear strength
# - the unconfined compression strength
# - the consistency classification
# - the calculations performed presented in a table

test = Analysis(data, calibrationFactor, length, diameter)
print("The area (in^2) of the sample is: ")
print(test.area())
print('\n')
test.add_properties()
print("The Stress vs. Strain plot: ")
test.plot_stress_vertical_strain()
print('\n')
print("Mohr plot: ")
test.plot_Mohr()
print('\n')
print("The peak strength (lb/in^2) of the sample is: ")
print(test.get_peak_strength())
print('\n')
test.classify_clay()
print('\n')
print("The following table displays the calculation results: ")
print(data)
