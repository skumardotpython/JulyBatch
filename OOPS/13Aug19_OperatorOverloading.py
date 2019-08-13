# class OperatorOverloading:
#
#     def Add(self, a, b):
#         c = a + b
#         print("Add is : ", c)
#
#
# ool = OperatorOverloading()
# ool.Add(10,20)
# ool.Add('Python', 'Tutorial')
#
# ool2 = OperatorOverloading()
# ool3 = ool + ool2

class vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b)


v1 = vector(10, 20)
v2 = vector(30, 40)

v3 = v1 + v2
print(v3)