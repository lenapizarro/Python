#! /usr/bin/env python 3
#Using shebang line

#This code is just a validation script

import platform

def main():
    helloWorldPrint()

def helloWorldPrint():
    print('Hello World!')
    print('This is python version {}'.format(platform.python_version()))

print('This function will print FIRST because is being called BEFORE main')

if __name__ == '__main__' : main()