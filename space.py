from maths import rev2deg
from numpy import array, ndarray, pi, cos, sin
from scipy.constants import gravitational_constant

K = 0.01720209895 # equals to the root of GM_s
SUN_MASS = 1.988e30 

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
    
    def get_gravity(self):
        return self.get_reduce_gravity()/self.mass_compare*SUN_MASS
    
    def get_mass(self) -> float:
        return self.get_reduce_gravity()/gravitational_constant

    def to_sun_vector(self, t_) -> ndarray:
        return self.to_sun*array([
            cos(rev2deg(t_, self.get_revolution())), 
            sin(rev2deg(t_/self.get_revolution())), 
            0])
    
    def get_hight_gravity(self, height_: float):
        return self.get_gravity()*(self.ray/(self.ray + height_))**2
    
class MorePlanete(Planete):
    def __init__(self, ray_, influence_,
                 density_: float, atmospheric_height_,
                 to_sun_ = 0, speed_ = 0, sun_mass_compare_ = 1):
        super().__init__(ray_, influence_, to_sun_, speed_, sun_mass_compare_)
        self.ground_density: float = density_
        self.atmospheric_height: int = atmospheric_height_

class Module:
    def __init__(self, mass_: float, drag_coefficient_: float, area_: float):
        self.mass: float = mass_
        self.drag_coefficient: float = drag_coefficient_
        self.area: float = area_

    def get_balisitical_factor(self):
        return self.mass/(self.drag_coefficient*self.area)
    
SUN = Planete(ray_=6.957e8, influence_=15e9)
EARTH = Planete(ray_=6378, influence_=9e5, to_sun_=150e6, speed_=29.78, sun_mass_compare_=1/332_946.0487)
JUPITER = Planete(ray_=69911, influence_=48.2e6, to_sun_=5.2026, speed_= 13.0585, sun_mass_compare_=1/1047.348625)