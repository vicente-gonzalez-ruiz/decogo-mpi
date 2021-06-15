'''
Seee https://hpc-forge.cineca.it/files/ScuolaCalcoloParallelo_WebDAV/public/anno-2016/25_Summer_School/Rome/mpi4py.pdf
'''
import os
from mpi4py import MPI

if __name__ == '__main__':
    # Instantiate the communicator
    comm = MPI.COMM_WORLD

    # Get the rank (id of the process)
    rank = comm.Get_rank()

    # Get the size (# of processes)
    size = comm.Get_size()
    print("I am rank number " + str(rank))

    if rank == 0:
        print("I am the master")
    else:
        print("Hello master! I am slave number " + str(rank))
