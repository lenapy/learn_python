def unique(iterable, seen=set()):
	"""accept iterable data and returns list of unique elements
	unique in sense unique hash"""
	acc = []
	for item in iterable:
		if item not in seen:
			seen.add(item)
			acc.append(item)
	return acc

def correct_unique(iterable, seen=None):
	seen = set(seen or []) # None --- falsy.
	acc = []
	for item in iterable:
		if item not in seen:
			seen.add(item)
			acc.append(item)
	return acc

if __name__ == '__main__':

	xs = [1, 1, 2, 3]

	print(unique(xs)) # prints [1, 2, 3]
	print(unique(xs)) # prints []

	print(unique.__defaults__) # prints ({1, 2, 3}, )

	print(correct_unique(xs)) # prints [1, 2, 3]
	print(correct_unique(xs)) # prints [1, 2, 3]
