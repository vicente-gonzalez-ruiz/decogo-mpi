from mpi4py import MPI
comm = MPI.COMM_WORLD

if comm.rank == 0:
    comm.send("Hello world", 1)

if comm.rank == 1:
    message = comm.recv()
    print("Rank 1 received '%s'" %
          message)
