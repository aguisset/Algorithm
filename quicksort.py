#!/usr/bin/env python

"""
Quicksort is a sorting algorithm that uses the Divide and Conquer paradigm to gain the same advantages as the merge sort, while not using additional storage.
As a trade-off, it is possible that the list may not be divided in half which might lead to the worst case performance.

Principle: 
----------
The algorithm selects an element (the pivot) in the array.
The array is partitioned (rearranged/divided) into two (possibly empty) subarrays such that each element in the first part is <= to the pivot (A[q]) which is, in turn, <= to each element of right part (A[q+1 ..r])
The quicksort algorithm is then recursively applied to the first part and the second part

Analysis: 
--------
The run-time is different whethever or not the array is balanced or not. The choice of the pivot is crucial.

worst case: O(n^2)
best case: O(nlogn)
average case: O(nlogn)

Note: Although the worst case is O(n^2) which is more than the other sorting algorithm, Quicksort is faster in practice than Merge Sort.
The reason behind this is that the inner-loops can be easily implemented on most architectures and in most real-world data.

Merge Sort is, however, considered better when dealing with huge amount of data or if the data are stored in an external storage

"""

# Main quickSort function that takes alist as a parameter
def quickSort(alist):
	quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
	if first < last:
		splitpoint = partition(alist, first, last)
		
		# Quicksort algorithm is recursively applied to the first part and second part
		quickSortHelper(alist, first, splitpoint -1)
		quickSortHelper(alist, splitpoint + 1, last)

# Example of partition where we take the first element as a pivot
def partition(alist, first, last):
	
	pivot_value = alist[first]
	
	leftmark = first + 1
	rightmark = last

	done = False

	# Loop until leftmark and rightmark converge
	while not done:

		while alist[leftmark] <= pivot_value and leftmark <= rightmark:
			leftmark = leftmark + 1


		while alist[rightmark] >= pivot_value and leftmark <= rightmark :
			rightmark = rightmark - 1

		# split point is found when leftmark and rightmark converge 
		if rightmark < leftmark:
			done = True

		else:
			# swapping
			alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

	# Changing the pivot with the rightmark_value	
	alist[first], alist[rightmark] = alist[rightmark], alist[first]

	return rightmark


# Test

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

