#
# class Calculator:
#
#     def Add(self, a, b):
#         print("Add is : ",  a + b)
#
# calc2 = Calculator()
# calc = Calculator()
# calc.Add(10, 20)
# calc.Add('Welcome ', 'Python')
# calc.Add(10.23, 11.26)
# # calc.Add(calc, calc2)

x = 10 + 10

class vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '%d, %d' % (self.a, self.b)

    def __add__(self, other):
        return  vector(self.a + other.a, self.b + other.b)



v1 = vector(10, 20)
v2 = vector(30, 40)

v3 = v1 + v2
print(v3.a)
print(v3.b)
print(v3)