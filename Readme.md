# Icarus

# Examples

- [Fidelity versus Finestructure splitting](http://nbviewer.ipython.org/urls/raw.github.com/eoinmurray/icarus/master/notebooks/Fidelity%2520verus%2520Fine%2520structure%2520splitting.ipynb)

- [Fidelity curves](http://nbviewer.ipython.org/urls/raw.github.com/eoinmurray/icarus/master/notebooks/Polarization%2520resolved%2520corrolation%2520curves.ipynb)

- [Monte carlo simulation of cross dephasing events](http://nbviewer.ipython.org/urls/raw.github.com/eoinmurray/icarus/master/notebooks/Pure%2520dephasing%2520monte%2520carlo.ipynb)

- [Degree of corrolation ratios between linear and diagonal basis](http://nbviewer.ipython.org/urls/raw.github.com/eoinmurray/icarus/master/notebooks/Degree%2520of%2520corrolation%2520ratios.ipynb)

- [Degree of corrolation ratio between linear and diagonal basis versus background emission level](http://nbviewer.ipython.org/urls/raw.github.com/eoinmurray/icarus/master/notebooks/Degree%2520of%2520corrolation%2520ratio%2520v%2520background.ipynb)

- [Antibunching g2 versus fine structure splitting](http://nbviewer.ipython.org/urls/raw.github.com/eoinmurray/icarus/master/notebooks/Auto%2520g2%2520vs%2520FSS.ipynb)

## Installation

Icarus depends on numpy and matplotlib so be sure to have those installed. If you have these then simply clone or [download](https://github.com/eoinmurray/icarus/archive/master.zip) the repo.

```sh
	git clone http://github.com/eoinmurray/icarus.git
	cd icarus
	python Experiments/fidelity.py
```

# PhotoLuminescence tools

## Constants
	
Class that holds the quantum dot and experiment parameters.

```python
	from constants import Constants
	constants = Constants()
```

## QuantumDot

```python
	from Icarus import QuantumDot
	qd = QuantumDot(constants.xtau, constants.xxtau, constants.ptau, constants.FSS, constants.crosstau)
```

## Detector

```python
	from Icarus import Detector
	detector = Detector(delay, efficiency, sigma, matrix)
```

## Channel

```python
	from Icarus import Channel
	channel = Channel(bin_width, detector1, detector2, name)
```

## PhotonCountingModule

```python
	from Icarus import PhotonCountingModule
	pcm = PhotonCountingModule()
	pcm.register_detector(name, detector)
	pcm.register_channel(name, channel)
```

## Laser

```python
	from Icarus import Laser
	laser = Laser(pulse_width, power)
```

## OpticalBench

```python
	from Icarus import OpticalBench
	opticalbench = OpticalBench()
```

## Spectrometer

```python
	from Icarus import Spectrometer
	spectrometer = Spectrometer()
```

# Algorithms

Icarus comes with three common experiments pre written, autocorrelation, cross-correlation and polarization resolved correlations.

## Auto correlation

## Cross correlation

## Polarization dependant correlation

# Experiment Manager

Icarus has an experiment manager that can be use to quickly set up one of the algorithms.
