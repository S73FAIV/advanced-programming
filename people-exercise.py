# Prepare a CSV file or spreadsheet with columns for the name, height, and weight of several people. 
# Upload it and calculate the average height of those above and below a given value.
# Also write down how many there are of each type.

import pandas

data = pandas.read_csv("exercise-persons.csv")

print("Enter Threshold for height:")
threshold = int(input("#"))

avg_height_above_threshold = data.height[data.height > threshold].mean()
number_of_people_above_threshold = data.height[data.height > threshold].count()

avg_height_below_threshold = data.height[data.height < threshold].mean()
number_of_people_below_threshold = data.height[data.height < threshold].count()

print("Threshold: ", threshold)
print("Data Shape: ", data.shape)
# print(data.describe())

print("Avg height above threshold: ", avg_height_above_threshold)
print("Number of people above threshold: ", number_of_people_above_threshold)
print("Avg height below threshold: ", avg_height_below_threshold)
print("Number of people above threshold: ", number_of_people_below_threshold)

## Add Body Mass Index BMI
# bmi = height**2 / weight

data['BMI'] = data.height**2 / data.weight
print("Data Shape: ", data.shape)
print(data)


