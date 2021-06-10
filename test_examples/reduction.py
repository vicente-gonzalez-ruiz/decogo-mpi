from mpi4py import MPI
from random import random 
comm = MPI.COMM_WORLD

t1 = MPI.Wtime()
count = 0
for i in range(comm.rank,100000,comm.size):
    (x,y) = (random(), random())
    if x * x + y * y < 1.0:
        count += 1

sum_count = comm.reduce(count, MPI.SUM)
t2 = MPI.Wtime()
print(t2 - t1)

if comm.rank == 0:
    print("pi = {}".format(4.0 * sum_count / 100000))
