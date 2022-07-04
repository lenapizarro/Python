#!/usr/bin/env python 3
#Using shebang line

#This code is just a validation script

import os
import platform
import sys

def main():
    helloWorldPrint()

def helloWorldPrint():
    print('Hello World!')
    print('This is python version {}'.format(platform.python_version()))
    print(sys.platform)
    print(os.getcwd())

print('This function will print FIRST because is being called BEFORE main')

if __name__ == '__main__' : main()   #This will return the name of the current module if someone were to import this file
