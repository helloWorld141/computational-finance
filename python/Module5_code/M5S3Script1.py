#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ncx2

#Variable declaration
S0 = 100
sigma = 0.3
gamma = 0.75
r = 0.1
T = 3
#Strikes to test volatility
test_strikes = np.linspace(80,120,41)