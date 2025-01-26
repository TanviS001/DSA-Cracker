# Problem statement
# You are given an array ‘Arr’ consisting of ‘N’ distinct integers and a positive integer ‘K’. 
# Find out Kth smallest and Kth largest element of the array. It is guaranteed that K is not greater than the size of the array.

def kthSmallLarge(arr, n, k):
    # Write your code here
    sorted_arr = sorted(arr)
    return [sorted_arr[k-1], sorted_arr[-k]]
    pass
