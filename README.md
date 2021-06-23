# decogo-mpi

An MPI implementation of the `decogo` solver.

## MPI and `mpi4py` installation

`decogo` is written in Python. Therefore, you need to install MPI and the Python's wrapper (mpi4py) in the system.

### Fedora 34

1. Install MPI.

There are two implementations for MPI: `mpich` and `openmpi`. We will use `mpich`. See also: https://docs.fedoraproject.org/en-US/neurofedora/mpi/

	sudo dnf install mpich mpich-devel

To use an MPI build, the appropriate environment module must be loaded. These correctly setup paths, and environment variables. For MPICH, run:

	module load mpi/mpich-x86_64

And it's a good idea to put it at the end of your `~/.bashrc`.

You can also try https://mpitutorial.com/tutorials/mpi-hello-world/ and see if everything is OK.

2. Install `mpi4py`:

For running Python, we will use `conda`.

	sudo dnf install conda
	
Now install `mpi4py` (https://pypi.org/project/mpi4py/) through `conda` but in a virtual environment:

	conda create --name EnvCondaDecogo
	conda activate EnvCondaDecogo # Remember: run "deactivate" to exit from the environment
	conda install mpi4py
	
Perform a minimal test:

	python -c "import mpi4py"

### Arch Linux

1. Install `openmpi`:

	sudo pacman -S openmpi
	
2. Install `mpi4py`:

	pip install mpi4py

## Installation of `decogo` and libraries

### Download `decogo`:

	git clone https://github.com/ouyang-w-19/decogo

### Install third party libraries for `decogo`:

1. Pyomo:

		pip3 install pyomo
		
2. Gurobi:

		sudo dnf install conda
		conda create --name EnvCondaDecogo
		conda activate EnvCondaDecogo
		conda config --add channels https://conda.anaconda.org/gurobi
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
			
<<<<<<< HEAD
	5. Add SCIP build/bin to $PATH in ~/.bashrc
		

##order of environment
To run decogo we habe to activate conda and after it pip3
	conda activate EnvCondaDecogo
	source EnvDECOGO/bin/activate
	
	 run...
	
=======
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

>>>>>>> c29a64af53e6a38899443ca3a1a0479bcf8fc3fc
	deactivate
	conda deactivate
	
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

