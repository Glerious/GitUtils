from numpy import sqrt, pi, ndarray, array, zeros
from enum import Enum

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
    
class EdoResolution:
    def __init__(self, func_: callable, 
                 a_: float, b_: float, 
                 init_: float | ndarray, 
                 N_: int = None, h_: float = None,
                 analytical_: callable = None) -> None:
        self.func = func_
        self.a = a_
        self.b = b_
        self.init = init_
        if h_ == N_ == None:
            raise Exception("Définition du pas nécéssaire.")
        if h_ == None:
            self.N = N_
            self.h = float((self.b - self.a) / self.N)
        else:
            self.h = h_
            self.N = int((self.b - self.a) / self.h)
        self.analytical = analytical_

    class Methods(Enum):
        EULER_EXPLICITE = 1
        RUNGE_KUTTA_2 = 2
        RUNGE_KUTTA_4 = 3

    def time_intervale(self) -> ndarray:
        return array([self.a + self.h * i for i in range(self.N + 1)])
    
    def initialise_methods(self) -> ndarray:
        _temp = array(self.init)
        _init = zeros((_temp.size, self.N + 1))
        _init[:, 0] = _temp
        return _init

    def euler_explicite(self) -> ndarray:
        y = self.initialise_methods()
        _start: bool = True
        for i, t in zip(range(len(self.time_intervale())), self.time_intervale()):
            if _start: 
                _start = False
                continue
            y[:, i] = y[:, i - 1] + self.h*self.func(t, y[:, i - 1])
        return y
    
    def runge_kutta_2(self) -> ndarray:
        ################################
        y_func = lambda t, y: y + self.h * self.func(t + 0.5*self.h, y + 0.5*self.h*self.func(t, y))
        ################################
        y = self.initialise_methods()
        _start: bool = True
        for i, t in zip(range(len(self.time_intervale())), self.time_intervale()):
            if _start: 
                _start = False
                continue
            y[:, i] =  y_func(t, y[:, i - 1])
        return y
    
    def runge_kutta_4(self) -> ndarray:
        y = self.initialise_methods()
        _start: bool = True
        for i, t in zip(range(len(self.time_intervale())), self.time_intervale()):
            if _start:
                _start = False
                continue
            _last_y = y[:, i - 1]
            _k1 = self.func(t, _last_y)
            _k2 = self.func(t + 0.5*self.h, _last_y + 0.5*self.h*_k1)
            _k3 = self.func(t + 0.5*self.h, _last_y + 0.5*self.h*_k2)
            _k4 = self.func(t + self.h, _last_y + self.h*_k3)
            y[:, i] = _last_y + self.h/6*(_k1 + 2*_k2 + 2*_k3 + _k4)
        return y
    
    def error(self, method: Methods) -> ndarray:
        # Find way to replace enum (enum code create bug to push)
        match method:
            case self.Methods.EULER_EXPLICITE:
                _result = self.euler_explicite()
            case self.Methods.RUNGE_KUTTA_2:
                _result = self.runge_kutta_2()
            case self.Methods.RUNGE_KUTTA_4:
                _result = self.runge_kutta_4()
        _error: list = []
        for i, t in zip(_result, self.time_intervale()):
            _error.append(abs(self.analytical(t) - i)/i)
        return _error
    
def rev2deg(rev_: float, base_: float) -> float:
    return 2*pi*rev_/base_

def deg2rev(deg_: float, base_: float) -> float:
    return base_*deg_/(2*pi)