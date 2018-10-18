import numpy as np
np.set_printoptions(suppress=True)
taxi = np.genfromtxt("nyc_taxis.csv", delimiter=",", skip_header=1)
# print(taxi[:10,:])

# If we compare an array to a comparison operator, it will return a boolean array of True/False values.
# print(taxi > 5)

# a = np.array([1, 2, 3, 4, 5])
# check_a = a < 3
# print(check_a)

# Boolean indexing is used to index (select) using a boolean arrary. This only selects the True values in the array:

# a_two = a[check_a]
# print(a_two)
# number_vals = a_two.shape[0] # The [0] extracts the value from the returned tuple of shape, as it is still a 2D array (I think?)
# print(number_vals)

# Can copy arrays using new_array = old_array.copy()
# print(a)
# a[a>3] = 10
# print(a)

# The above first selects from array a all values >3, and changes them to 10.
# this also would work if A was a 2D array, would replace all values >3 with 10.
# A function like: c[c[:,1] > 2, 1] = 99
# The above looks at 2D array C, and for the first column with values above 2, it changes the values to 99.

# bool = array[:, column_for_comparison] == value_for_comparison
# array[bool, column_for_assignment] = new_value

# Or, in one line:
# array[array[:, column_for_comparison] == value_for_comparison, column_for_assignment] = new_value

# The below code firstly clones taxi, creates a zero column at 15 for a new variable, by creating the column of zeros and concatenating.
# Then, a boolean array is created, looking at the 5th column (location), and if it equals an airport, it is True.
# All true values have their column 15 as 1.
# Airport location codes are 2 (JFK), 3 (LaGuardia), 5 (Newark)

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()

# create a new column filled with `0`.
zeros = np.zeros([taxi_modified.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
# print(taxi_modified)

boolarr = taxi_modified[:,5] == 2
taxi_modified[boolarr, 15] = 1

boolarr = taxi_modified[:,5] == 3
taxi_modified[boolarr, 15] = 1

boolarr = taxi_modified[:,5] == 5
taxi_modified[boolarr, 15] = 1

# array[array[:, column_for_comparison] == value_for_comparison, column_for_assignment] = new_value
# Just to select certain values:
# new_array = array[array[:, column_for_comparison] == value_for_comparison]


trip_mph = taxi[:,7] / (taxi[:,8] / 3600) # Created a new array for miles per hour
cleaned_taxi = taxi[trip_mph < 100]  # Filtered the taxi data, only with results of avg mph < 100
# column 7 = trip distance, 8 = trip length, 13 = total amount.
# Basically, we wanted to remove error data i.e. removing all average mph > 100.


mean_distance = cleaned_taxi[:,7].mean()
mean_length = np.mean(cleaned_taxi[:,8])
mean_total_amount = np.mean(cleaned_taxi[:,13])
mean_mph = np.mean(trip_mph[trip_mph < 100])

print(mean_distance)
print(mean_length)
print(mean_total_amount)
print(mean_mph)
