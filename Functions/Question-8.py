 '''Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20'''
  #ANSWER:-
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))
