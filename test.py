from source import Analysis

# Import your inital CSV data file
# This example is from the data table from my Input File
data = pd.read_csv('Unconfined_Compression_Test_InitialData.csv')
data


# This next set of code is so that the user can input their specific parameters for the calculations
# This includes the calibration factor, the length of the sample, and the diameter of the sample
# The input function will allow for easier calculations since everyone will have different parameters
calibrationFactor = float(input("Calibration Factor: "))
length = float(input("Length in inches: "))
diameter = float(input("Diameter in inches: "))


# This is where the class is instantiated and the functions are called
# The outputs given are:
#the area of the sample,
#the Stress vs. Vertical Strain Curve,
#the unconfined compression strength,
#and the consistency classification
test = Analysis(data, calibrationFactor, length, diameter)
print(test.area())
test.add_properties()
test.plot_stress_vertical_strain()
print(test.get_peak_strength())
test.classify_clay()
