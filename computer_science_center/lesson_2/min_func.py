def bounded_min(first, *args, lo=float("-inf"), hi=float("inf")):
	res = hi
	for arg in (first, ) + args:
		if arg < res and lo < arg < hi:
			res = arg
	return max(res, lo)


if __name__ == '__main__':
	min = bounded_min(-5, 12, 13, lo=0, hi=255)
	print(min)