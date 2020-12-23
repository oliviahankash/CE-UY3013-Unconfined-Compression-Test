# CE-UY3013-Unconfined-Compression-Test
*To solve the calculations for the Unconfined Compression Test and classify the soil sample*

This program analyzes the data from an Unconfined Compression Test for clay soil specimens. This Test is important because it is important to know the unconfined compression strength in deciding what type of soil to use.

Assumptions:

* Clay soil sample


Inputs:

* A CSV containing file containing the Deformation (inches) and Dial Reading measurements from your Unconfined Compression Test experiment
* The input folder also includes sample parameter input values that are used in my example


Outputs:

* the area of the sample
* the unconfined compression strength of the sample
* the classification of the consistency of the clay
* the Stress vs. Vertical Strain Curve
* the calculations of the experiment presented in one table
* Mohr’s Circle for Unconfined Compression Test that locates the undrained shear strength


## Set Up

* To use the program, you have to clone/download this repository and navigate to the local directory.
* Create and activate the virtual environment you choose.
* Install the required libraries for this program with:
` install requirements.txt `


## How to Use the Program

When you begin running the project, make sure you have your CSV file uploaded and ready to import with your two columns of data: Deformation and Dial Reading.

While running the program, Python will prompt you to input your own data for the parameters. The parameters include the calibration factor, the length of the sample, and the diameter of the sample.

After the parameters are inputted, the program will continue to make the necessary calculations. It will also plot the curve of Stress vs. Vertical Strain.

By the end of the program, the unconfined compression strength is determined. The sample will be classified according to its consistency classification and stated. The Stress vs. Vertical Strain plot is displayed. The calculations performed in the code will be presented in a final table. Mohr’s Circle for Unconfined Compression Test that locates the undrained shear strength is also demonstrated at the end.
