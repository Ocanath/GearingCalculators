from helical_centerdistance import *

h = HelicalGears()
print(h.radial_pressure_angle_rad*180/np.pi)

val = np.pi/6
inv = h.involute(np.pi/6)

print("input", val)
print("involute", inv)
print("inverse involute", h.inverseInvolute(inv))