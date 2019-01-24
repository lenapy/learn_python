"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""
from itertools import combinations
def main(lst, k):
	for comb in combinations(lst, 2):
		if sum(comb) != k:
			continue
		else:
			return True
	return False

if __name__ == '__main__':
	l = [10, 15, 3, 7]
	k = 17
	res = main(l, k)
	print(res)