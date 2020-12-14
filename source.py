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
