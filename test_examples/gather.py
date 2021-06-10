from mpi4py import MPI
comm = MPI.COMM_WORLD

data = comm.rank
gathered_data = comm.gather(data, root=0)

if comm.rank == 0:
    print("rank:", comm.rank, "data:", gathered_data)
    print("rank:", comm.rank, "data:", data)
else:
    print("rank:", comm.rank, "data:", data)
