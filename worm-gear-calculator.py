from WormGear import *

w = WormGearPair(module=0.45, num_starts=3, num_teeth=22, pitch_diameter=6,pressure_angle=20.0)
w.coefficient_of_friction = 0.16
print("root diameter", w.d_r)
print("lead", w.L)
print("worm wheel diameter", w.D)
print("worm lead at mean diameter", w.lead_angle_at_mean_diameter*180/np.pi, "deg")
print("worm lead at mean diameter, radians", w.lead_angle_at_mean_diameter)
print("Number of teeth required", w.check_min_teeth_condition())
e = w.get_efficiency()
print("efficiency", e)
print("is theoretically backdrivable?", w.is_backdrivable())