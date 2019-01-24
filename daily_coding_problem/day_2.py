"""This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the
product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?"""

from functools import reduce


def main(array):
	new_array = []
	for i in range(len(array)):
		temp_arr = array[:i] + array[i+1:]
		el = reduce(lambda x, y: x*y, temp_arr)
		new_array.append(el)
	return new_array

if __name__ == '__main__':
	arr= [1, 2, 3, 4, 5]
	new_array = main(arr)
	print(new_array)
