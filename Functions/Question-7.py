'''Write a Python function to find the Max of three numbers.'''
  #ANSWER:-
def maxoftwo( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, maxoftwo( y, z ) )
print(maxofthree(3, 6, -5))
