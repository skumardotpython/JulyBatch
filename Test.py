class Calculaltor:

    globalVaribale = 100

    def __init__(self, a, b):
        self.a = a   # Class Variable or Instance Variable
        self.b = b
        result = a + b # Local Variable (The scope of the variable is limited within the function)


    def Add(self):
        c = self.a + self.b
        print('The sum is :', c)


    def Sub(self):
        c = self.a - self.b
        print('The Sub is :', c)

    def Mul(self):
        c = self.a * self.b
        print('The Mul is :', c)

    def Div(self):
        c = self.a / self.b
        print('The Div is :', c)


calc = Calculaltor(20,10)

calc.Add()
calc.Sub()
calc.Mul()
calc.Div()
calc.Add()

print('*' * 100)

cal = Calculaltor(30,10)
cal.Add()