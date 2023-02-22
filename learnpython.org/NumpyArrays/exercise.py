# Tutorial exercise

# Covert the list of weights from a list to a Numpy array.
# Convert all of the weights from kg to lbs
# Use the scalar coversion 2.2lbs per kg
# Print the array of weights in pounds

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)    

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)
