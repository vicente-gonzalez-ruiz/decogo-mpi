# parallel.py
# https://pyomo.readthedocs.io/en/stable/working_models.html#solving-multiple-instances-in-parallel
# run with mpirun -np 2 python -m mpi4py parallel.py
import pyomo.environ as pyo
from mpi4py import MPI

rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
assert size == 2, 'This example only works with 2 processes; please us mpirun -np 2 python -m mpi4py parallel.py'

# Create a solver
#opt = pyo.SolverFactory('cplex_direct')
opt = pyo.SolverFactory('glpk')

#
# A simple model with binary variables
#
model = pyo.ConcreteModel()
model.x = pyo.Var([1,2], domain=pyo.NonNegativeReals)
model.obj = pyo.Objective(expr = 2*model.x[1] + 3*model.x[2])
model.Constraint1 = pyo.Constraint(expr = 3*model.x[1] + 4*model.x[2] >= 1)

if rank == 1:
    model.x[1].fix(1)

results = opt.solve(model)
print('rank: ', rank, '    objective: ', pyo.value(model.obj.expr))
