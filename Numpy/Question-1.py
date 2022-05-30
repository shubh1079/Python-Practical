'''Write a NumPy program to repeat all the elements three times of a given
array of string'''
  #ANSWER:-
import numpy as np
x1 = np.array(['Python', 'PHP', 'Java', 'C++'], dtype=np.str)
print("Original Array:")
print(x1)
newarray = np.char.multiply(x1, 3)
print("New array:")
print(newarray)
