# Exercise 4: Classifying and converting temperatures

The exercise for this week is meant to help you to understand how to use functions in Python.
In this week's exercise you are asked to create a simple tool that converts temperatures from
one temperature-type to another and then classify those temperatures into specific temperature classes.

After making your changes, you will need to upload your files to GitHub.
The answers to the questions in this week's exercise should be given by modifying the document in places where asked.

- **Exercise 4 is due by the start of lecture on 3.10.**
- Don't forget to check out [the hints for this week's exercise](https://geo-python.github.io/2018/lessons/L4/exercise-4-hints.html) if you're having trouble.
- Scores on this exercise are out of 20 points.

## Problem 0 - Mid-term course feedback requested

Before you get started on the exercise, we'd like for you to take 5 minutes to provide us with some feedback on how the course is going so far.
This is the second time we're teaching the course in this format, and we would be very pleased to have your honest thoughts (positive or negative) about how things are going.
Feedback is **completely anonymous**.

[**Course feedback e-form**](https://elomake.helsinki.fi/lomakkeet/92231/lomake.html)

## Problem 1 - Simple temperature calculator (6 points)

In the first problem your aim is to create a function that converts the input temperature from degrees Fahrenheit to degrees Celsius. Follow closely the instructions and use **exactly** the same variable, function, and parameter names as stated in the instructions because we use automatic grading to check your codes.

**Start Problem 1 by cloning this repo to cloud computer and opening the following notebook**:
 
  - [Exercise-4-problem-1.ipynb](Exercise-4-problem-1.ipynb)

## Problem 2 (*7 points*)

In the [last week's exercise (Problem 2)](https://github.com/Geo-Python-2018/Exercise-3/blob/master/Exercise-3-problem-2.ipynb) we practiced how to classify temperatures
into four different classes (*i.e. cold, slippery, comfortable, warm*). Let's continue working with the same idea. Here, you should create a function that
accepts a temperature value in Celsius that will be reclassified into integer numbers 0-3 based on following criteria:

 | Return value | Classification criteria                  |
 |---|-----------------------------------------------------|
 | 0 | temperatures below -2 degrees (Celsius)             |
 | 1 | temperatures equal or higher than -2 up to +2 degrees (Celsius)  |
 | 2 | temperatures equal or higher than +2 up to +15 degrees (Celsius)  |
 | 3 | temperatures equal or higher than +15 degrees (Celsius)            |
 
**Start Problem 2 by opening the following notebook**:
 
  - [Exercise-4-problem-2.ipynb](Exercise-4-problem-2.ipynb)
  
## Problem 3 - Classify temperatures (7 points)

Finally, we can bring together the pieces that we have created thus far. In the last problem your aim is to take
advantage of your new functions and reclassify a dataset of temperatures in Fahrenheit into four different classes.

The temperature values are provided below and they look like following:

  ```
  # List of half-hourly temperature values (in degrees Fahrenheit) for one week
  # Showing first two rows
  tempData = [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 34, 34,
               34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27, 27, 27, 23, 23, ]
  ```

### Overview

The analysis process has three main steps:

 1. Read in the data from the data cell (execute it) and iterate over the Fahrenheit temperatures.
 2. Convert the Fahrenheit temperature to Celsius using your `fahr_to_celsius` function from that was created in Problem 1.
 3. Classify the converted temperature using the `temp_classifier` function that was created in Problem 2.
 
**Start Problem 3 by opening the following notebook**:
 
  - [Exercise-4-problem-3.ipynb](Exercise-4-problem-3.ipynb)
