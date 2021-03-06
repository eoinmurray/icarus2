


import numpy as np



def cross(qd, pcm, laser, bench, spectrometer, constants):
	"""
		Crosscorrolation experiment algorithm.
	"""

	for time in laser.pulseTimes(constants.integration_time):	
		xxtrue, xtrue = qd.emission(laser.power) 
		xlifetime, xxlifetime = qd.generate_lifetimes()
		poptime = qd.poptime()
		
		if not constants.poptime_on:
			poptime = 0

		if xxtrue:
			pcm.detector('D3').hit(time, xxlifetime)

		if xtrue:	
			pcm.detector('D1').hit(time, xlifetime)
		
			xxtrue, xtrue = qd.emission(laser.power*constants.secondary_emission_probability) 
			time_2 = time + xlifetime + poptime
			xlifetime, xxlifetime = qd.generate_lifetimes()
			poptime = qd.poptime()
						
			if not constants.poptime_on:
				poptime = 0
		
			if xtrue:
					pcm.detector('D1').hit(time_2, xlifetime + poptime)