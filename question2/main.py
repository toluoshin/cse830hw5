#Python script to test different k values for Tim sort

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

    #return arr


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
def insertionSort(arr, l, r):
    for i in range(l, r+1):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timSort(arr, l, r, k):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        if m-l < k:
            insertionSort(arr, l, m)
        else:
            timSort(arr, l, m, k)
        if r-m < k:
            insertionSort(arr, m+1, r)
        else:
            timSort(arr, m + 1, r, k)

        merge(arr, l, m, r)

n = 1
tim_results = [[] for i in range(9)]
n_list = []

while n < 200:
    temp_tim = [[] for i in range(9)]
    for i in range(9):
        arr1 = []
        for i in range(n):
            arr1.append(random.randint(0, 1000))
        for k_val in range(9):
            arr2 = arr1.copy()
            before_tim = timeit.default_timer()
            timSort(arr2, 0, n-1, k_val*25)
            tim_time = timeit.default_timer() - before_tim
            temp_tim[k_val].append(tim_time * pow(10, 3))
    for k in range(9):
        tim_results[k].append(sum(temp_tim[k]) / len(temp_tim[k]))
    n_list.append(n)
    n+=1

print(n_list)
print(tim_results)

for k in range(9):
    plt.plot(n_list, tim_results[k], label = "tim sort, k = " + str(k*25))

plt.title("Comparison of tim sorts")
plt.xlabel("Length of array")
plt.ylabel("Time to sort (milliseconds)")

plt.legend()
plt.show()
