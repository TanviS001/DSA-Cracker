  #Problem statement
  #Given an array/list 'ARR' of integers and a position ‘M’. You have to reverse the array after that position.
  
  #Example:
  
  #We have an array ARR = {1, 2, 3, 4, 5, 6} and M = 3 , considering 0 
  #based indexing so the subarray {5, 6} will be reversed and our 
  #output array will be {1, 2, 3, 4, 6, 5}. 
 

from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    length = len(arr)
    p = m+1
    q = length-1

    while p<q:
        temp=arr[p]
        arr[p]=arr[q]
        arr[q]=temp

        p+=1
        q-=1
    return arr
