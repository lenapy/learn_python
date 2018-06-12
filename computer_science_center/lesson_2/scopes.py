def wrapper():
	def identity(x):
		return x
	return identity


def make_min(*, lo, hi):
	def inner(first, *args):
		res = hi
		for arg in (first, ) + args:
			if arg < res and lo < arg < hi:
				res = arg
		return max(res, lo)
	return inner

def func():
	min = 2
	print(locals())

def cell(value=None):
	def get():
		return value
	def set(update):
		nonlocal value
		value = update
	return get, set

if __name__ == '__main__':
	f  = wrapper()
	res = f(42)
	print(res) # 42

	bounded_min = make_min(lo=0, hi=255)
	bounded_min(-5, 12, 13)

	min = 42
	print(globals()) # {..., 'min': 42}

	print(func()) # {'min': 42}

	get, set = cell()
	set(42)
	print(get())