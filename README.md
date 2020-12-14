# CE-UY3013-Unconfined-Compression-Test
To solve the calculations for the Unconfined Compression Test and classify the soil sample

This program analyzes the data from an Unconfined Compression Test for clay soil specimens. This Test is important because it is important to know the unconfined compression strength in deciding what type of soil to use, such as choosing the best material for an embankment.

Assumptions:

* Clay soil sample


Inputs:

* A CSV containing file containing the Deformation (inches) and Dial Reading measurements from the Unconfined Compression Test experiment


Outputs:

* the unconfined compression strength of the sample
* the classification of the consistency of the clay


## Set Up

* To use the program, you have to clone/download this repository and navigate to the local directory.
* Create and activate the virtual environment you choose.
* Install the required libraries for this program with:
` <$ pip install -r requirements.txt>`


## How to Use the Program

When you begin running the project, make sure you have your CSV file uploaded to import with your two columns of data: Deformation and Dial Reading.

While running the program, Python will prompt you to input your own data for the parameters. This includes the calibration factor, length of the sample, and diameter of the sample.

After the parameters are inputted, the program will continue to make the necessary calculations. It will then plot the curve of Stress vs. Vertical Strain.

By the end of the program, the unconfined compression strength is determined. The sample will then be classified according to its consistency classification.
