import numpy as np


class HelicalGears:
	z1 = 0	#number of teeth
	z2 = 0	#number of teeth
	m = 0	#normal module
	helix_angle_rad = 0	#commonly beta, in RADIANS
	normal_pressure_angle_rad = 0	#alpha_n, in RADIANS

	def __init(self, num_teeth_1=10,num_teeth_2=20,normal_module=1,helix_angle_deg=30,normal_pressure_angle_deg=20):
		self.z1 = num_teeth_1
		self.z2 = num_teeth_2
		self.m = normal_module
		self.helix_angle_rad = helix_angle_deg*np.pi/180
		self.normal_pressure_angle_rad = normal_pressure_angle_deg*np.pi/180

		self.radial_pressure_angle_rad = np.arctan(np.tan(self.normal_pressure_angle_rad)/np.cos(self.helix_angle_rad))
		self.y = (self.z1+self.z2)/(2*np.cos(self.helix_angle_rad))*(  np.cos(self.radial_pressure_angle_rad)/np.cos(alpha_w_t) - 1  )

		