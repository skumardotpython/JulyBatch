class Celsius:

    def __init__(self, temperature = 0):
        self.temperature = temperature

    def set_temperature(self, value):
        if(value < - 273):
            raise ValueError("the value cannot be less than -273")
        self._temperature = value

    def get_temperature(self):
        return self._temperature

    def to_fahrenheit(self):
        return ((self.temperature * 1.8) + 32)

    temperature = property(get_temperature,set_temperature)

cs = Celsius()
cs.temperature = 50
print(cs.temperature)