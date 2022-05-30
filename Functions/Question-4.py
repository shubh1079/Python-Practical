'''WAP in pyhton to find the prime number in a given range using function'''
 #ANSWER
def prime(a,b):
    for i in range(a,b+1,1):
        c=0
    for j in range(1,i+1,1):
        if i%j==0:
            c+=1
            if c==2:
                print(i,end='')
print("enter the range")
a=int(input("enter a number\n"))
b=int(input("enter a number\n"))
prime(a,b)
