'''Write a Python function to check whether a number falls in a given range'''
  #ANSWER:-
def testrange(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
testrange(5)
