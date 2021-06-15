# decogo-mpi
A MPI test cases for decogo solver.

## MPI and `mpi4py` installation

First install MPI in the system.

### Fedora 34
See howto install and execute mpich:

https://docs.fedoraproject.org/en-US/neurofedora/mpi/

Select `mpich`. `openmpi` version is also available.

	root$> dnf install mpich mpich-devel

To use an MPI build, the appropriate environment module must be loaded. These correctly setup paths, and environment variables. For MPICH builds:

	$> module load mpi/mpich-x86_64

Better to put it on `/etc/bashrc`.

Then check it with:

https://mpitutorial.com/tutorials/mpi-hello-world/

Then, you can install `mpi4py` on the system:

	root$> dnf install python3-mpi4py-mpich.x86_64
	root$> dnf install mpi4py-docs.noarch
	
Docs are in `/usr/share/doc/mpi4py-docs`.

To install `mpi4py` with `pip3`:

	$>pip3 install mpi4py
	
It needs in the system `pyhton3-devel` and I think `mpich` working as well.

Also installled:

	$>pip3 install whell 

https://pypi.org/project/mpi4py/

Please remember to load the correct module for your choosen MPI environment

	$>module load mpi/mpich-x86_64
	$>python -c "import mpi4py"

### Arch Linux

1. Install `openmpi`:

	sudo pacman -S openmpi
	
2. Install `mpi4py`:

	pip install mpi4py
