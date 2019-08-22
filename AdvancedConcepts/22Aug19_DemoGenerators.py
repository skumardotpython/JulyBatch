# The difference is that, while a return statement terminates a function entirely,
# yield statement pauses the function saving all its states and later continues
# from there on successive calls.


# Differences between Generator function and a Normal function
# Here is how a generator function differs from a normal function.
#
# Generator function contains one or more yield statement.
# When called, it returns an object (iterator) but does not start execution immediately.
# Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.


def GeneratorFunction():
    n = 1
    print("First Statement Execution")
    yield n

    n = 2
    print("Second Statement Execution")
    yield n

    n = 3
    print("Third Statement Execution")
    yield n

    n = 4
    print("Fourth Statement Execution")
    yield n


yieldValue = GeneratorFunction()
print(next(yieldValue))
print(next(yieldValue))
print(next(yieldValue))
print(next(yieldValue))

foo = open('test.txt', 'r')
value = foo.read(10)
print(value)
value = foo.read(10)
print(value)
value = foo.read(10)
print(value)
value = foo.read(10)
print(value)