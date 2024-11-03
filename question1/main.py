# Python script to compare merge sort and insertion sort

import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

# Function to sort array using insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code
n = 1
merge_results = []
insertion_results = []
n_list = []

while n < 200:
    temp_merge = []
    temp_insertion = []
    for i in range(100):
        arr1 = []
        for i in range(n):
            arr1.append(random.randint(0, 1000))
        arr2 = arr1.copy()

        before_merge = timeit.default_timer()
        mergeSort(arr1, 0, n-1)
        merge_time = timeit.default_timer() - before_merge

        before_insertion = timeit.default_timer()
        insertionSort(arr2)
        insertion_time = timeit.default_timer() - before_insertion

        temp_merge.append(merge_time * pow(10, 3))
        temp_insertion.append(insertion_time * pow(10, 3))

    merge_results.append(sum(temp_merge)/len(temp_merge))
    insertion_results.append(sum(temp_insertion)/len(temp_insertion))
    n_list.append(n)
    n+=1

print(n_list)
print(merge_results)
print(insertion_results)

plt.plot(n_list, merge_results, label = "merge sort")
plt.plot(n_list, insertion_results, label = "insertion sort")
plt.legend()
plt.show()
