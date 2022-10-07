import copy
import os
import pickle
import gc
import time
import torch, gpytorch
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

def main(args=None):

    use_GPU = True   
    use_On = True

    predictor_class = NLMPCPredictor    # Either None or one of trajectory_predictor classes
    use_predictions_from_module = True  # Set to true to use predictions generated from `predictor_class`, otherwise use true predictions from MPCC

    M = 10  # Number of samples for GP
    n_inducing_pts = 50
    T = 100 # Max number of seconds to run experiment
    t = 0  # Initial time increment

