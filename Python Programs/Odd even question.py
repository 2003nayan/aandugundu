#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = input("Enter the number: ")

    n = int(n)
    
    if n%2 != 0:
        print("Weird")
        
    if n%2 == 0:
        if 2<n<5:
            print("Not Weird")
            
        if 6<n<20:
            print("Weird")
            
        if n<20:
            print("Not Weird")