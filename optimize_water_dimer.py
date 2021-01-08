import numpy as np
from scipy import optimize
from pyvibdmc.simulation_utilities import *
from pyvibdmc.simulation_utilities import potential_manager as pm

h4o2_coord_raw = np.array([[1.513632,   -0.005249,   -0.121857],
                                [0.560102,    0.002812,    0.048059],
                                [1.913196,    0.033035,    0.750687],
                                [-1.385643,    0.004325,    0.110302],
                                [-1.750594,    0.746224,   -0.382028],
                                [-1.746613,   -0.774680,   -0.324277]])
								
pot_dir = '../Potentials/legacy_mbpol/' 
py_file = 'call_mbpol.py'
pot_func = 'call_single_dimer' # does not loop, takes in a 6x3 array and outputs energy

x = Constants.convert(h4o2_coord_raw,'angstroms',to_AU=True)
ps_oh = pm.Potential(potential_function=pot_func,
                               python_file=py_file,
                               potential_directory=pot_dir,
                               num_cores=1
                        )

from optimizer import Geometry_Optimizer
x = Constants.convert(h4o2_coord_raw,'angstroms',to_AU=True)

print("begin_geom", Constants.convert(x,'angstroms',to_AU=False))

optim = Geometry_Optimizer(p_manager = ps_oh, 
                           coord = x)
final_geom = optim.minimize()

print("final_geom", Constants.convert(final_geom,'angstroms',to_AU=False))