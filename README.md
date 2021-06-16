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

	$>pip3 install wheel 

https://pypi.org/project/mpi4py/

Please remember to load the correct module for your choosen MPI environment

	$>module load mpi/mpich-x86_64
	$>python -c "import mpi4py"

### Arch Linux

1. Install `openmpi`:

	sudo pacman -S openmpi
	
2. Install `mpi4py`:

	pip install mpi4py

## Installation of `decogo` and libraries

### Set the environment

1. Download `decogo`:

		clone git: https://github.com/ouyang-w-19/decogo

2. Create a virtual environment for Python:

		cd decogo
		python3 -m venv EnvDECOGO
		
3. Activate:

		source EnvDECOGO/bin/activate
		pip3 freeze
		
4. (Optional) de-activate:

		desactivate

### Build the documentation:

1. `graphviz`:

		pip3 install graphviz
		
2. `sphinx` and `sphinx_rtd_theme`:

		pip3 install  sphinx
		pip3 install sphinx_rtd_theme
		
3. Make:

		make html
		
4. Open:

		cd _build/html
		open index.html

### Install third party libraries for `decogo`:

1. Pyomo:

		pip3 install pyomo
		
2. Gurobi:

		dnf install conda
		conda create --name EnvCondaDecogo
		conda activate EnvCondaDecogo
		conda install gurobi
		
3. IPOPT:

		dnf install coin-or-Ipopt.x86_64 coin-or-Ipopt-devel coin-or-Ipopt-mpich-devel
		
4. SCIP:

	1. Create a directory for compiling the source code:
	
			mkdir Packages
			cd SCIP
			mkdir SCIP

	2. Download the sources from https://www.scipopt.org/index.php#download
	
	3. Install the packages:
	
			dnf install boost.x86_64 boost-devel.x86_64  # Also install  boost-mpich-devel and boost-mpich-python3
			dnf install cliquer-libs cliquer-devel       # Cliquer is a set of C routines for finding cliques in an arbitrary weighted graph.
			dnf install lapack-devel.x86_64              # Also install scalapack-mpich scalapack-mpich-devel
			dnf install glslang-devel                    # Official reference compiler front end for the OpenGL
			dnf install readline-devel                   # The Readline library provides a set of functions that allow users to edit command lines.
			dnf install gmp-devel                        # The gmp package contains GNU MP, a library for arbitrary precision arithmetic, signed integers operations, rational numbers and floating point numbers.
			dnf install bliss bliss-devel                # Bliss is an open source tool for computing automorphism groups and canonical forms of graphs.
			dnf install gsl gsl-devel                    # The GNU Scientific Library (GSL) is a collection of routines for numerical analysis, written in C.
			
			
			# I seems hMetis is an optinal package for SCIP. It has to be installed from tgz.
			
			# Download hMetis from http://glaros.dtc.umn.edu/gkhome/metis/hmetis/download into DECOGO/Packages/hMetis/hmetis-1.5-linux
			
			ln -s hmetis2.0pre1 hmetis
			
			# And include this path in the PATH: in ~/bashrc or in ~/bin which is at the $PATH

	4. Compile SCIP:
	
			cd cd DECOGO/Packages/SCIP
			mkdir build
			cd build
			cmake ..
			make
			
			# libs and binaries are at:
			# DECOGO/Packages/SCIP/scipoptsuite-7.0.3/build/bin and
			# DECOGO/Packages/SCIP/scipoptsuite-7.0.3/build/lib
		
	5. Add:
	
			DECOGO/Packages/SCIP/scipoptsuite-7.0.3/build/bin
			
	   to your PATH, and make this change permanent modifiying for example `~/.bashrc`.
	   
	6. Install some extra libraries:
	
			pip3 install networkx numpy scipy sympy
			pip3 install pslib pyutilib

## Environments activation:

	conda activate EnvCondaDecogo
	source EnvDECOGO/bin/activate

## Environments deactivation:

	deactivate
	conda deactivate
