# This is the beginning of me making my class for the analysis calculations

class Analysis:

# First I have to initialize the object with csvfiledata, the calibration factor, the length of the sample, and the diameter of the sample
    def __init__(self, csvFileData, calibrationFactor, length, diameter):
        self.data = csvFileData
        self.calibrationFactor = calibrationFactor
        self.length = length
        self.diameter = diameter


# This function will calculate the area of the sample. It is done by using the input diameter
    def area(self):
        return ((math.pi)/4)*(self.diameter)**2


# This function will calculate the vertical strain, load, area, and stress of the sample
# It is done using the data from the CSV file, as well as the input paramters
# They are also added to the dataframe so that it is all in one combined table
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
