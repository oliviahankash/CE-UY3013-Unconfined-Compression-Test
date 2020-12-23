# -- Imports ------------------------------------------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import interpolate

# This is the beginning of me making my class for the analysis calculations

# Necessary imports for code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import interpolate

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

# These next three lines plot the point of the peak stress represented by the red point
        ymax = max(self.data['Stress (lb/in2)'])
        xmax = x[y.argmax()]
        plt.plot(xmax, ymax, 'ro', color = 'red' , label = 'unconfined compression strength (lb/in^2)')

# These next lines are for the titles, labels, and design of the plot itslef
        plt.title('Stress vs. Vertical Strain', fontweight='black', fontfamily='monospace')
        plt.xlabel('Vertical Strain')
        plt.ylabel('Stress (lb/in2)')
        plt.grid(ls='-')
        plt.legend(loc="lower right")
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



# The following code will plot Mohr’s Circle for the Unconfined Compression Test
# The x-axis is the Normal Stress (lb/in2)
# The y-axis is the Shear Stress (lb/in2)

    def plot_Mohr(self):
# Cu is the undrained shear strength
      Cu = 0.5 * max(self.data['Stress (lb/in2)'])
      x = [0,Cu, max(self.data['Stress (lb/in2)'])]
      y=[0,Cu, 0]
      x2 = np.linspace(x[0], x[-1], 100)
      y2 = interpolate.pchip_interpolate(x, y, x2)
      plt.plot(x2, y2, color = 'blue')
      plt.plot(x, y, "ro", color = 'red')

# The following three codes are for the sake of specifying and labeling what the three points represent
      plt.plot(Cu , Cu , 'ro', color = 'red', label = 'undrained shear strength' )
      plt.plot(0 , 0, 'ro', color = 'green', label = 'normal stress failure'  )
      plt.plot(max(self.data['Stress (lb/in2)']) , 0, 'ro', color = 'purple' , label = 'unconfined compression strength' )

# These next lines are for the titles, labels, and design of the plot itslef
      plt.title('Mohr’s Circle for Unconfined Compression Test', fontweight='black', fontfamily='monospace')
      plt.xlabel('Normal Stress (lb/in2)')
      plt.ylabel('Shear Stress (lb/in2)')
      plt.grid(ls='-')
      plt.legend(loc="lower center")
      plt.show()

 # This is the end of the class Analysis
