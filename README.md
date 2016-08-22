# Join Charts with Seaborn

This IBM SPSS Modeler extension enables Joint Distribution Plots to be generated using Python and Stanford University's Seaborn library.

The Plots allow bivariate distributions to be visualized, using a main plot covering both variables and two margin plots convering each individual variable.

The following plot types are supported:

* Regression: Scatter plot with a regression line
![image](https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/screenshots/regression.png)
* Scatter
![image](https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/screenshots/scatter.png)
* Hex Binning
![image](https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/screenshots/hexbin.png)
* Kernrel Density Estimation
![image](https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/screenshots/kde.png)

Learn more about this implementation [from the Seaborn Documentation][4]

![Stream](https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/screenshots/stream.png)

---
Requirements
----
- SPSS Modeler v18.0 or later
- [Python 2.7 Anaconda Distribution 4.1.1 or later](https://www.continuum.io/downloads)
- Seaborn package - install the seaborn package into your Anaconda installation using Anaconda command: conda install seaborn

More information here: [IBM Predictive Extensions][2]

---
Installation Instructions
----

#### Initial one-time set-up for PySpark Extensions

If using v18.0 of SPSS Modeler, navigate to the options.cfg file (Windows default path: C:\Program Files\IBM\SPSS\Modeler\18.0\config).  Open this file in a text editor and paste the following text at the bottom of the document:

  eas_pyspark_python_path, "*C:/Users/IBM_ADMIN/Anaconda/python.exe*"

  -   The italicized path should be replaced with the path to your python.exe from your Anaconda installation.

#### Extension Hub Installation
  1. Go to the Extension menu in Modeler and click "Extension Hub"
  2.	In the search bar, type the name of this extension and press enter
  3. Check the box next to "Get extension" and click OK at the bottom of the screen
  4. The extension will install and a pop-up will show what palette it was installed to

#### Manual Installation
  1.	[Save the .mpe file][3] to your computer
  2.	In Modeler, click the Extensions menu, then click Install Local Extension Bundle
  3.	Navigate to where the .mpe was saved and click open
  4.	The extension will install and a pop-up will show what palette it was installed

---
Example
----

[Download the example stream][5]
[Download the example data][6]

---
License
----

[Apache 2.0][1]

---
Contributors
----
- Niall McCarroll - ([www.mccarroll.net](http://www.mccarroll.net/))


[1]:http://www.apache.org/licenses/LICENSE-2.0.html
[2]:https://developer.ibm.com/predictiveanalytics/downloads
[3]:https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/SeabornJointPlot.mpe
[4]:https://stanford.edu/~mwaskom/software/seaborn/index.html
[5]:https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/example/example.str
[6]:https://raw.githubusercontent.com/IBMPredictiveAnalytics/JointPlots_with_Seaborn/master/example/iris.csv
