''' Write a NumPy program to capitalize the first letter, lowercase, uppercase, swapcase, title-case of all the elements of a given array.'''
 #ANSWER:-
import numpy as np
x = np.array(['python', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
capitalized_case = np.char.capitalize(x)
lowered_case = np.char.lower(x)
uppered_case = np.char.upper(x)
swapcased_case = np.char.swapcase(x)
titlecased_case = np.char.title(x)
print("\nCapitalized: ", capitalized_case)
print("Lowered: ", lowered_case)
print("Uppered: ", uppered_case)
print("Swapcased: ", swapcased_case)
print("Titlecased: ", titlecased_case)
