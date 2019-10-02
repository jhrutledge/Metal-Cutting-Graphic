README
TITLE : Orthogonal Cutting Graphic
AUTHOR : jhrutledge

DEPENDENCIES:
 - Python 3.7
 - Numpy
 - Tkinter
 - PyInstaller

DESCRIPTION :
This project creates an object to calculate parameters relevant to orthogonal 
cutting based on its geometric principles. The results are shown numerically 
and graphically. Parameters relating to velocity and energy can also be 
calculated and shown numerically and graphically.

TABS :
 README
  - description of project and each tab included
 Force Calculations
  - list of variables relating to orthogonal cutting and the merchant circle
  - calculates remaining values when proper input set is given
  - press "Update" to process inputs
 Merchant Circle
  - dynamic diagram of results from Force Calculations tab
 Power Caclulations
  - list of variables relating to energy in orthogonal cutting
  - inputs are drawn from Force Calculations tab and user
  - calculates "Outputs" when proper input set is given
  - press "Update" to process inputs
 Chip Diagram
  - dynamic diagram of parameters from Force and Power Calculations tabs
 Angle Diagram
  - static diagram to explain layout of angles around tool tip

INCLUDED FILES :
 - README.txt
 - CuttingGraphic.py
   - main python script, must be run with python3 in same directory as 
	 README.txt and CaclulationClasses.py
 - CalculationClasses.py
   - contains python classes to build GUI and complete calculations
 - mac executable [FOLDER]
 - windows executable [FOLDER]
   - executable files are located within the "dist" folder and named 
     CuttingGraphic
 
NOTE:
 - mac executable files were unable to be compiled
 - executables were created with pyinstaller
 - Dimensions alternative to those listed in the graphic can be supplied 
   for accurate result so long as relationship between forces and angles 
   is the same.