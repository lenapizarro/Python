#!/usr/bin/env python3

def main():
    file = open('BunchOfLines.txt', 'r+')   #no need to add all the path, since they are in the same folder. The default mode is read-only. a is append, w is write (it erases everything in the file to write it again)
    for line in file:
        print(line.rstrip())


if __name__ == '__main__' : main() 


#"r"   Opens a file for reading only.
#"r+"  Opens a file for both reading and writing.
#"rb"  Opens a file for reading only in binary format.
#"rb+" Opens a file for both reading and writing in binary format.
#"w"   Opens a file for writing only.
#"a"   Open for writing. The file is created if it does not exist.
#"a+"  Open for reading and writing.  The file is created if it does not exist.