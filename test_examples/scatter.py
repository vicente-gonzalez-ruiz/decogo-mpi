from mpi4py import MPI
comm = MPI.COMM_WORLD

if comm.rank == 0:
    data = [1,2,3,4]
else:
    data = None

data = comm.scatter(data)
print("rank:", comm.rank, "data:", data)
