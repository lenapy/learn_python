import sys

def trace(func):
	def inner(*args, **kwargs):
		print(func.__name__, args, kwargs)
		return func(*args, **kwargs)
	return inner

def identity(x):
	"I do nothing useful"
	return x

print(identity.__name__, identity.__doc__) # will print out: identity I do nothing useful

identity = trace(identity)

print(identity.__name__, identity.__doc__) # will print out: inner None

#-----------------------------------------------------------------------------------------------------------------------

def identity_v2(x):
	"I do nothing useful"
	return x

def trace_v2(func):
	def inner(*args, **kwargs):
		print(func.__name__, args, kwargs)
		return func(*args, **kwargs)
	inner.__name__ = func.__name__
	inner.__module__ = func.__module__
	inner.__doc__ = func.__doc__
	return inner

print(identity_v2.__name__, identity_v2.__doc__) # will print out: identity I do nothing useful

@trace_v2
def identity_v2(x):
	"I do nothing useful"
	return x

print(identity_v2.__name__, identity_v2.__doc__) # will print out: inner None

#-----------------------------------------------------------------------------------------------------------------------

import functools

def identity_v3(x):
	"I do nothing useful"
	return x

def trace_v3(func):
	def inner(*args, **kwargs):
		print(func.__name__, args, kwargs)
		return func(*args, **kwargs)
	functools.update_wrapper(inner, func)
	return inner

def trace_v4(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		print(func.__name__, args, kwargs)
		return func(*args, **kwargs)
	return inner

#-----------------------------------------------------------------------------------------------------------------------

trace_enable = False

def trace_v5(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		print(func.__name__, args, kwargs)
		return func(*args, **kwargs)
	return inner if trace_enable else func

#-----------------------------------------------------------------------------------------------------------------------

def trace_v6(handle):
	def decorator(func):
		@functools.wraps(func)
		def inner(*args, **kwargs):
			print(func.__name__, args, kwargs, file=handle)
			return func(*args, **kwargs)
		return inner
	return decorator


@trace_v6(sys.stderr)
def identity(x):
	return x

deco = trace_v6(sys.stderr)
identity = deco(identity)

#-----------------------------------------------------------------------------------------------------------------------

# **use help for this

def with_arguments(deco):
	@functools.wraps(deco)
	def wrapper(*dargs, **dkwargs):
		def decorator(func):
			result = deco(func, *dargs, **dkwargs)
			functools.update_wrapper(result, func)
			return result
		return decorator
	return wrapper

@with_arguments
def trace_v7(func, handle):
	def inner(*args, **kwargs):
		print(func.__name__, args, kwargs, file=handle)
		return func(*args, **kwargs)
	return inner

@trace_v7(sys.stderr)
def identity(x):
	return x