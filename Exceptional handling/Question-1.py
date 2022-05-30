'''WAP in python  to depict Raising Exception'''
#ANSWER:-
try:
	raise NameError("Hi there") 
except NameError:
	print ("An exception")
	raise 
