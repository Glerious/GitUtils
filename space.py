from maths import rev2deg

from numpy import array, ndarray, pi, cos, sin

G = 6.67384e-11
K = 0.017_202_098_95 # equals to the root of GM_s   

class Planete:
    def __init__(self, ray_: int, influence_: int,
                 to_sun_: int = 0, speed_: float = 0,
                 sun_mass_compare_: float = 1):
        self.mass_compare: float = sun_mass_compare_
        self.ray: int = ray_
        self.to_sun: int = to_sun_
        self.spherical_influence: int = influence_
        self.speed: int = speed_

    def get_revolution(self) -> float:
        return 4*pi**2*self.to_sun**3/K**2

    def get_reduce_gravity(self) -> float:
        return K**2/self.mass_compare
    
    def get_mass(self) -> float:
        return self.get_reduce_gravity()/G

    def to_sun_vector(self, t_) -> ndarray:
        return self.to_sun*array([
            cos(rev2deg(t_, self.get_revolution())), 
            sin(rev2deg(t_/self.get_revolution())), 
            0])
    
SUN = Planete(ray_=6.957e8, influence_=15e9)
EARTH = Planete(ray_=6378, influence_=9e5, to_sun_=150e6, speed_=29.78, sun_mass_compare_=1/332_946.0487, )
JUPITER = Planete(ray_=69911, influence_=48.2e6, to_sun_=5.2026, speed_= 13.0585, sun_mass_compare_=1/1047.348625)