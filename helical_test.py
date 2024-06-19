from helical_centerdistance import *
import matplotlib.pyplot as plt

"""
Note: NORMAL module is different from TRANSVERSE module. Transverse module is defined as normal module times cosine of beta
"""

# h = HelicalGears(profile_shift_1=0.09809)
h = HelicalGears(num_teeth_1=28,num_teeth_2=12,normal_module=0.4,helix_angle_deg=30,normal_pressure_angle_deg=20,profile_shift_1=0,profile_shift_2=0)
print("radial pressure angle, degrees", h.radial_pressure_angle_rad*180/np.pi)
print("radial working pressure angle, degrees", h.radial_working_pressure_angle_rad*180/np.pi)
print("y", h.y)
print("center distance", h.ax)

# val = 22*np.pi/180
# print("input", val)
# # print("involute", inv)
# print("inverse involute", h.inverseInvolute(val))
# print("inverse involute of involute of val", h.inverseInvolute(h.involute(val)))

