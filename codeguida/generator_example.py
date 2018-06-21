def func():
    print("> Why doesn't this line print?")
    exit() # Within this function, nothing should matter after this point.  The program should exit
    yield "> The exit line above will exit ONLY if you comment out this line."

x = func() #  since func() is a generator, a generator iterator is returned.
#  So while that may look like a function call,
# it's actually giving us the generator iterator we would use to generate values yielded by the generator.

x.__next__()

