from helical_centerdistance import *
import matplotlib.pyplot as plt

"""
Note: NORMAL module is different from TRANSVERSE module. Transverse module is defined as normal module times cosine of beta
"""

# h = HelicalGears(profile_shift_1=0.09809)
transverse_module = 0.4
helix_angle = 30
normal_module = transverse_module*np.cos(helix_angle*np.pi/180)
h = HelicalGears(num_teeth_1=-28,num_teeth_2=68,normal_module=normal_module,helix_angle_deg=helix_angle,normal_pressure_angle_deg=20,profile_shift_1=0,profile_shift_2=0)
print("radial pressure angle, degrees", h.radial_pressure_angle_rad*180/np.pi)
print("radial working pressure angle, degrees", h.radial_working_pressure_angle_rad*180/np.pi)
print("y", h.y)
print("center distance", h.ax)

# val = 22*np.pi/180
# print("input", val)
# # print("involute", inv)
# print("inverse involute", h.inverseInvolute(val))
# print("inverse involute of involute of val", h.inverseInvolute(h.involute(val)))
print("x1 = ", h.ax*np.cos(0*120*np.pi/180+np.pi/2), "y1 = ", h.ax*np.sin(0*120*np.pi/180+np.pi/2))
print("x2 = ", h.ax*np.cos(120*np.pi/180+np.pi/2), "y2 = ", h.ax*np.sin(120*np.pi/180+np.pi/2))
print("x3 = ", h.ax*np.cos(2*120*np.pi/180+np.pi/2), "y3 = ", h.ax*np.sin(2*120*np.pi/180+np.pi/2))