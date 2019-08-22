#
#
# A function defined inside another function is called a nested function.
# Nested functions can access variables of the enclosing scope.
#
# In Python, these non-local variables are read only by default and we must
# declare them explicitly as non-local (using nonlocal keyword) in order to modify them.

# 1. Nested Functions are called as Closures
# 2. Parent Function parameter can be called with in your child function
# 3. Invoke the child function within your parent function
# 4. Closure can be stored in a variable and can be passed as a parameter to another function
# 5. Parmeter function can be fired with in any function

def parentfunction(parParm):

    print('Parent Function Called')

    def childfunction():
        print(parParm)

    childfunction()

def InvokeClosureFunction(func):

    func('Invoking with in a function')

funcVariable = parentfunction
# funcVariable('Initial Value')
InvokeClosureFunction(funcVariable)



