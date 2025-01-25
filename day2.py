# Problem Statement:
# You are given an array “ARR” of size N. Your task is to find out the sum of maximum and minimum elements in the array.

from os import *
from sys import *
from collections import *
from math import *

def sumOfMaxMin(arr):
    # Write your code here
    min_num=min(arr)
    max_num=max(arr)

    return min_num+max_num
    
