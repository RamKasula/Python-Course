# 	Create an array from a range of values from 1 to 20 incrementing by 2

import numpy as np

a = np.arange(1,20,2)
print(a)

# Print the data type of the array created  above.
print(a.dtype)

# Print the size of the array created above.
print(a.size)

# Reshape the array created above to 5 Rows and 2 columns
b =  a.reshape(5,2)
print(b)

# Find and print the MAX / MIN / AVG / SUM of each row
print (b.max(axis=1))
print (b.min(axis=1))
print (b.mean(axis=1))
print (b.sum(axis=1))

# Find and print the MAX / MIN / AVG / SUM of each column
print (b.max(axis=0))
print (b.min(axis=0))
print (b.mean(axis=0))
print (b.sum(axis=0))

# Create a multi-dimensional array consisting of 2 instances of 4 rows and 4 columns full of 0s.
c = np.zeros((2,4,4))
print(c)

# Create a multi-dimensional array consisting of 4 instances of 5 rows and 3 columns full of random numbers.
random_set = np.random.random((4,5,3))
print(random_set)
