"""Examples for object oriented programming."""

import math

class Complex():
    """ Class for complex numbers """

    def __init__(self, a:float, b:float) -> None:
        """ Constructor for complex """
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f'{self.a} + j{self.b}'
    
    def __add__(self, other):
        c = Complex(self.a + other.a, self.b + other.b)
        return c
    
    def __sub__(self, other):
        c = Complex(self.a - other.a, self.b - other.b)
        return c
    
    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b*other.a)
    
    def __truediv__(self, other):
        r1, phi1 = self.polar()
        r2, phi2 = other.polar()
        r = r1 / r2
        phi = phi1 - phi2
        return Complex(r * math.cos(phi), r * math.sin(phi))
    
    def polar(self):
        r = math.sqrt(self.a * self.a + self.b * self.b)
        phi = math.atan2(self.b, self.a)
        return r, phi
    



def main():
    x = Complex(0.5, 0.5)
    y = Complex(1.0, 0.5)
    print(f'Wert von x = {x - y}')
    

if __name__ == '__main__':
	main()
