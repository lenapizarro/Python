#!/usr/bin/env python 3


def main():
    print('Hello, World!'.capitalize())
    print('Hello, World!'.upper())
    print('Hello, World!'.title())
    print('Hello, World!'.swapcase())

    s1 = 'Hello'
    s2 = 'World! I\'m done.'
    s3 = s1 + ' ' + s2

    print(s3)

    x = 15 * 2641.0
    y = 2230
    print('The result is {:,}'.format(x)) # the semicolon is used as the format instruction set
    print('The result is {:b}'.format(y))  # binary

    print(f'The result is {y:b}')   #using f strings 
    print(s3.split()) #splits words
    print(s3.split('l')) #splits when finds an l

if __name__ == '__main__' : main() 