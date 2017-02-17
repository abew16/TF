# TF

This Repository contains all drills relating to the TF Prep Course.

Prep Capstone 

Instructions:
Run the file 'Prep_Capstone_UnX.py'
To run in Unix use:
>>>python3 Prep_Capstone_UnX.py

Proposal:
This data set shows whether an individual either makes more or less than 50K per year and factors which may effect that (age, education, race, sex, etc…). The data is from the 2014 census.
My goal is to show what level of education someone must have in order to have a 50% probability of having an income greater than 50K

Implementation techniques:
Initially, I use a bar and pie chart to show the amounts of the sample per education level. From there I will use t-tests from Scipy to evaluate if we should accept that a certain education level will give you a 50% chance of having an income above 50K.    

Issues/problems that occurred 
Initially I built and tested the program on my local machine which runs Windows 10 with the intention of moving it to Unix. SciPy is not available for Windows so the program must be run on Unix in order for the hypothesis tests to work.

There were also issues running the module Pyvttbl, which is used to create the ANOVA table. The code is still in the program commented out for the future.


hypothesis test conclusion on the proposal
In order to reject the null hypothesis for the alternative (>50% chance to have a >50K income) the t-test must be positive and the P-Value must be below .1 at a 10% significance level.
