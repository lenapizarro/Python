#!/usr/bin/env python 3

#Testing classes in python

import platform

class Cow:
    sound = "Mooo!"
    walks = "Walks slowly like a cute cow."

    def moo(self):
        print(self.sound)

    def walk(self):
        print(self.walks)

 
def main():
    Lola = Cow()
    Lola.moo()
    Lola.walk()
    #print('Hello, my name is:{}'.format(Cow().__name__))

if __name__ == '__main__' : main()