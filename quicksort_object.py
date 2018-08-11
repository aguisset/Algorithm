#!/usr/bin/env python

"""

With minor adaptations from: https://github.com/donnemartin/interactive-coding-challenges


Constraints:
	1) Naive solution sufficient (ie not in-place)
	2) Are duplicates allowed? Yes
	3) Can we assume the input is valid? No
	4) Can we assume this fits memory? Yes


"""

# if you want to use the float type division
# from __future__ import division

class QuickSort(object):

	def sort(self, data):

		# See constraints 3
		if data is None:
			raise TypeError('data is None')

		return self.sortHelper(data)


	def sortHelper(self, data):

		# Check if there is one element in the array
		if len(data) < 2:
			return data


		equal = []
		left = []
		right = []

		pivot_index = (len(data)-1)/2
		pivot_value = data[pivot_index]

		# Loop to build the left and right partition
		for item in data:
			if item == pivot_value:
				equal.append(item)

			elif item <= pivot_value:
				left.append(item)

			else:

				right.append(item)

		# Recursively apply quick_sort

		left_new = self.sortHelper(left)
		right_new = self.sortHelper(right)

		return left_new + equal + right_new

