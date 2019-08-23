def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    # result = func(x)
    # return result
    print(func(x))


incrVar = inc
dectVar = dec


operate(incrVar, 10)
# print(operate(incrVar, 5))
# print(operate(dectVar, 5))


