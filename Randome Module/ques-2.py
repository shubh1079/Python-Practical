#WAP in Python to generate a random alphabetical character, alphabetical string and alphabetical string of a fixed length
#ANS:-
import random
import string
print("Generate a random alphabetical character:")
print(random.choice(string.ascii_letters))
print("\nGenerate a random alphabetical string:")
max_length = 255
str1 = ""
for i in range(random.randint(1, max_length)):
    str1 += random.choice(string.ascii_letters)
print(str1)
print("\nGenerate a random alphabetical string of a fixed length:")
str1 = ""
for i in range(10):
    str1 += random.choice(string.ascii_letters)
print(str1)
