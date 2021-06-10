from mpi4py import MPI
comm = MPI.COMM_WORLD

# Alice; say Hello to Bob
if comm.rank == 0:
    comm.send("Hello Bob!", 1)
    mesg = comm.recv()
    print("Alice: Bob said {}".format(mesg))

# Bob; say Hello to Alice
if comm.rank == 1:
    comm.send("Hello Alice!", 0)
    mesg = comm.recv()
    print("Bob: Alice said {}".format(mesg))
