

import numpy as np

class Constants():
	# Quantum dot
	xtau = 1
	xxtau = 0.5
	ptau = 2
	poptime_on = False
	FSS = 0e-6
	hbar = 6.58e-16
	secondary_emission = True
	secondary_emission_probability = 0.18

	# Laser
	pulse_width = 25.
	power = 0.5

	# Detector
	FWHM = 4.8
	sigma = FWHM/(2*np.sqrt(np.log(2)*2))
	efficiency = 1
	delay = 161.8
	bin_width = 50

	# Experiment parameters
	num_iterations = 1
	integration_time = 100000