'''WAP in python to check whether the number is palindrome or not'''
  #ANSWER:-
def palindrome(p):
        a=input('enter the no.')
        p=a[::-1]
        if(a==p):
                print('palindrome')
        else:
                print('not')
palindrome(121)
