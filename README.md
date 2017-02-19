# TF

This Repository contains all drills relating to the TF Prep Course.

Author:

##Prep Capstone Project
This project is intended to explore the concepts of data science and is a preliminary to the complete Capstone project for Thinkful Data Science Bootcamp

###Data Science Concepts:
Investigated and explored the topics of hypothesis testing and data visualization as well as deepening my knowledge of Python.  

###Instructions:
file of interest(s):

 - Prep_Capstone_UnX.py

Installation:

	>>>npm ..

Run the script:
	
	>>>python3 Prep_Capstone_UnX.py

###Environment and Dependencies:

	- Ubuntu 16.04.1
	- Python 3.5
	- numpy 1.12.0
	- scipy 0.18.1
	- matplotlib 1.5.1

###Proposal:
This data set shows whether an individual either makes more or less than 50K per year and factors which may effect that (age, education, race, sex, etc…). The data is from the 2014 census.
My goal is to show what level of education someone must have in order to have a 50% probability of having an income greater than 50K

###Implementation techniques:


###Procedures:
Initially, I use a bar and pie chart to show the amounts of the sample per education level. From there I will use t-tests from Scipy to evaluate if we should accept that a certain education level will give you a 50% chance of having an income above 50K. I used a random sample of 1000 people from the data set.

###Findings:





![education charts](https://cloud.githubusercontent.com/assets/25283369/23106278/a8484f6e-f69f-11e6-9cc4-9985468b0b82.png)

![Percentage of Sample >50K Income](https://cloud.githubusercontent.com/assets/25283369/23105880/884b7ff6-f69a-11e6-8bcc-b6b8369ffbee.PNG)

In order to reject the null hypothesis for the alternative (>50% chance to have a >50K income) the t-test must be positive and the P-Value must be below .1 at a 10% significance level.

As you can see from the table below, only a doctorate or professional degree has enough evidence to show that there is a greater than 50% chance to have a 50K income. 

![Hypothesis Tests](https://cloud.githubusercontent.com/assets/25283369/23105877/859670fe-f69a-11e6-9984-55edbb4bd533.PNG)


###Issues and Problems: 
The issues and problems that occurred are that initially I built and tested the program on my local machine which runs Windows 10 with the intention of moving it to Unix. SciPy is not available for Windows so the program must be run on Unix in order for the hypothesis tests to work.




Code Issues:  
An example of the code issues I came across..


There were also issues running the module Pyvttbl, which is used to create the ANOVA table. The code is still in the program commented out for the future.

    "firstName": {
        ".validate":"newData.isString()"
    },
    "lastName": {
        ".validate":"newData.isString()"
    },
    "phoneNumber": {
        ".validate":"newData.isString() && newData.val().length == 11"
    }

###Conclusion:
What overall findings through your research did you come across and what conclusions do you have.  Post numbers and image here too for reference.
