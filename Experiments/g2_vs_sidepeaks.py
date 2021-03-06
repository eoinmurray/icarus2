


import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import numpy as np
import matplotlib.pyplot as plt
from constants import Constants
import Icarus.Experiment as Experiment	



if __name__ == "__main__":
	"""
		Records the corrolation sidepeaks during the experiment.
	"""
			
	hold_side = []
	hold_g2   = []
	
	constants = Constants()
	experiment = Experiment(constants, Visualizer=True)
	def echo(object):
		experiment.pcm.channel('D1D3').processPeaks(experiment.laser.pulse_width)
		g2   = experiment.pcm.channel('D1D3').get_g2()
		side = experiment.pcm.channel('D1D3').get_sidepeaks_avg()
		hold_g2.append(g2)
		hold_side.append(side)

	experiment.on('tick', echo)
	experiment.run('basis')

	plt.ioff()
	plt.close('all')
	plt.plot(hold_side, hold_g2, 'b-')
	plt.ylim([0, np.max(hold_g2)+0.5])
	plt.show()

	plt.xlim([0, 300])
	plt.plot(experiment.pcm.channel('D1D3').bin_edges, experiment.pcm.channel('D1D3').counts)
	plt.show()

