import numpy as np



class HelicalGears:
	z1 = 0	#number of teeth
	z2 = 0	#number of teeth
	m = 0	#normal module
	helix_angle_rad = 0	#commonly beta, in RADIANS
	normal_pressure_angle_rad = 0	#alpha_n, in RADIANS
	Xn1 = 0	#normal coefficient of profile shift gear 1
	Xn2 = 0 #normal coefficient of profile shift gear 2
	

	def __init__(self, num_teeth_1=10,num_teeth_2=20,normal_module=1,helix_angle_deg=30,normal_pressure_angle_deg=20):
		self.z1 = num_teeth_1
		self.z2 = num_teeth_2
		self.m = normal_module
		self.helix_angle_rad = helix_angle_deg*np.pi/180
		self.normal_pressure_angle_rad = normal_pressure_angle_deg*np.pi/180

		self.radial_pressure_angle_rad = np.arctan(np.tan(self.normal_pressure_angle_rad)/np.cos(self.helix_angle_rad))

		
		# self.alpha_w_t = self.inverseInvolute(0)
		# self.y = (self.z1+self.z2)/(2*np.cos(self.helix_angle_rad))*(  np.cos(self.radial_pressure_angle_rad)/np.cos(self.alpha_w_t) - 1  )

		
	def involute(self, x):
		return np.tan(x) - x
	
	def inverseInvolute(self, x):
		maxError = 0.0000001
		guess = 0.1
		high = np.pi/2
		low = 0

		for i in range(0,1000000000000):
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