#WAP in python  to read an entire text file.
#ANS:-
def file_read(fname):
        txt = open(fname)
        print(txt.read())
file_read('test.txt')
