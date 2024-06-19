import numpy as np



"""
NOTE:
IF you're doing a planetary gearset with profile shift, ensure the 
number of teeth in the RING gear is POSITIVE and the number of teeth in the PLANET gear is NEGATIVE

I.e 68T ring and 28T planet, z1 = 68, z2 = -28
SHould work
^^DOES NOT WORK. the standard pitch diameter of a helical ring gear is different

Also, helixangle = 0 should make this work for spur planetaries
"""

class HelicalGears:
	z1 = 0	#number of teeth
	z2 = 0	#number of teeth
	m = 0	#normal module
	helix_angle_rad = 0	#commonly beta, in RADIANS
	normal_pressure_angle_rad = 0	#alpha_n, in RADIANS
	Xn1 = 0	#normal coefficient of profile shift gear 1
	Xn2 = 0 #normal coefficient of profile shift gear 2
	

	def __init__(self, num_teeth_1=12,num_teeth_2=60,normal_module=3,helix_angle_deg=30,normal_pressure_angle_deg=20, profile_shift_1=0, profile_shift_2=0):
		self.z1 = num_teeth_1
		self.z2 = num_teeth_2
		self.m = normal_module
		self.helix_angle_rad = helix_angle_deg*np.pi/180
		self.normal_pressure_angle_rad = normal_pressure_angle_deg*np.pi/180
		self.Xn1 = profile_shift_1
		self.Xn2 = profile_shift_2
		self.compute_params()

		
	def involute(self, x):
		return np.tan(x) - x
	
	def inverseInvolute(self, x):
		maxError = 0.0000000000001
		guess = 0.1
		high = np.pi/2
		low = 0

		for i in range(0,10000000000000):
			chk = self.involute(guess)
			if(chk > x):
				high = guess
				guess = (guess + low) / 2
			else:
				low = guess
				guess = (guess + high) / 2
			if(chk - x < maxError and chk - x > -maxError):
				return guess			
		return guess
	
	def computeWorkingRadialPressureAngle(self):
		inv_awt = 2*np.tan(self.normal_pressure_angle_rad * ((self.Xn1 + self.Xn2)/(self.z1 + self.z2)) ) + self.involute(self.radial_pressure_angle_rad)
		if(self.Xn1 != 0 or self.Xn2 != 0):
			self.radial_working_pressure_angle_rad = self.inverseInvolute(inv_awt)
		else:
			self.radial_working_pressure_angle_rad = self.radial_pressure_angle_rad	#if there is no profile shift, the working pressure angle is equal to the radial pressure angle
		return self.radial_working_pressure_angle_rad
	
	def get_working_pitch_diameter(self, z, m, beta_rad):
		return (z*m)/np.cos(beta_rad)

	def compute_params(self):
		self.radial_pressure_angle_rad = np.arctan(np.tan(self.normal_pressure_angle_rad)/np.cos(self.helix_angle_rad))
		self.computeWorkingRadialPressureAngle()
		self.y = ((self.z1+self.z2)/(2*np.cos(self.helix_angle_rad)))*(  np.cos(self.radial_pressure_angle_rad)/np.cos(self.radial_working_pressure_angle_rad) - 1  )
		self.ax	= ((self.z1 + self.z2)/(2*np.cos(self.helix_angle_rad)) + self.y) *self.m	#Center Distance!!!!
		self.d1 = self.get_working_pitch_diameter(self.z1, self.m, self.helix_angle_rad)	#standard pitch diameter
		self.d2 = self.get_working_pitch_diameter(self.z2, self.m, self.helix_angle_rad)	#standard pitch diameter

