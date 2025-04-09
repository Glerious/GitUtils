from numpy import sqrt, pi

class Deg2Resolv:
    def __init__(self, a_: float, b_: float, c_: float):
        self.a: float = a_
        self.b: float = b_
        self.c: float = c_
    
    def discriminant(self) -> float:
        return self.b**2 - 4*self.a*self.c
    
    def root(self) -> tuple:
        _left = -self.b/(2*self.a)
        _right = sqrt(self.discriminant())/(2*self.a)
        # _left, _right /= (2*self.a) TODO find way to do that
        if self.discriminant() < 0: _right = 1j*_right
        return(_left + _right, _left - _right)
    
def rev2deg(rev_: float, base_: float) -> float:
    return 2*pi*rev_/base_

def deg2rev(deg_: float, base_: float) -> float:
    return base_*deg_/(2*pi)
    
