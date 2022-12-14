from simulator.simulator import Simulator
import sys

# command line args
grid_id = int(sys.argv[1])
pol_type = sys.argv[2]

# define a simulator object
simulator = Simulator()
simulator.execute(0, grid_id, pol_type)
