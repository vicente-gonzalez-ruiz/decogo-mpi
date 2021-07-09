# decogo-mpi

A MPI implementation of the `decogo` solver. The search space is splitted into blocks and each one is processed in parallel using a master-slave scheme.

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
	conda activate EnvCondaDecogo # Remember: run "conda deactivate" to exit from the environment
	conda install mpi4py
	
Perform a minimal test:

	python -c "import mpi4py"

### Arch Linux

1. Install `openmpi`:

	sudo pacman -S openmpi
	
2. Install `mpi4py` (notice that `gcc` must be installed):

	pip install mpi4py

## Installation of `decogo` and libraries

### Download `decogo`:

	git clone https://github.com/ouyang-w-19/decogo

### Install third party libraries for `decogo`:

1. Pyomo (see https://anaconda.org/conda-forge/pyomo):

	# Be sure to be in the virtual environment
	conda install -c conda-forge pyomo
	
2. Solvers:

	* (Optional) GNU Linear Programming Kit:
	
	pacman -S glpk # Arch Linux
		
	* Gurobi:

  		1. Register and create a academic license:
  
  			open https://www.gurobi.com/downloads/end-user-license-agreement-academic/

  		2. Download the executables from https://www.gurobi.com/downloads/ (Gurobi Optimizer):
  
    		1. Go to https://www.gurobi.com/academia/academic-program-and-licenses/ and download the executables:
    
    			cd ~/DECOGO
    			mkdir packages
    			cd packages
    			wget https://packages.gurobi.com/9.1/gurobi9.1.2_linux64.tar.gz
    	
  		3. Update the enviroment variables:
  
  			export GUROBI_HOME="$HOME/DECOGO/packages/gurobi912/linux64"
			export PATH="$GUROBI_HOME/bin:$PATH"
			export LD_LIBRARY_PATH="$GUROBI_HOME/lib:$LD_LIBRARY_PATH"

  		4. Create the license (https://www.gurobi.com/downloads/free-academic-license/):
  
  			cd ~/DECOGO/packages/gurobi912/linux64/bin
  			grbgetkey 62d6019e-d415-11eb-a08e-0242ac120002

  		5. Install the Python binding (see https://www.gurobi.com/documentation/9.1/quickstart_mac/cs_anaconda_and_grb_conda_.html):

			# Be sure to be in the virtual environment
			conda config --add channels https://conda.anaconda.org/gurobi
			conda install gurobi
		
	* IPOPT (see https://coin-or.github.io/Ipopt/INSTALL.html, notice that this is a system-wide install):

		sudo dnf install coin-or-Ipopt.x86_64 coin-or-Ipopt-devel coin-or-Ipopt-mpich-devel
		conda install psutil pyutilib numpy scipy networkx pandas psutil

	* SCIP:

  		1. Create a directory for compiling the source code:
	
			mkdir Packages
			mkdir SCIP
			cd SCIP

  		2. Download and untar the sources from https://www.scipopt.org/index.php#download
  
			tar xvf scip-7.0.3.tgz
	
  		3. Install the packages:
	
			# Fedora
			sudo dnf install boost.x86_64 boost-devel.x86_64  # Also install  boost-mpich-devel and boost-mpich-python3
			sudo dnf install cliquer-libs cliquer-devel       # Cliquer is a set of C routines for finding cliques in an arbitrary weighted graph.
			sudo dnf install lapack-devel.x86_64              # Also install scalapack-mpich scalapack-mpich-devel
			sudo dnf install glslang-devel                    # Official reference compiler front end for the OpenGL
			sudo dnf install readline-devel                   # The Readline library provides a set of functions that allow users to edit command lines.
			sudo dnf install gmp-devel                        # The gmp package contains GNU MP, a library for arbitrary precision arithmetic, signed integers operations, rational numbers and floating point numbers.
			sudo dnf install bliss bliss-devel                # Bliss is an open source tool for computing automorphism groups and canonical forms of graphs.
			sudo dnf install gsl gsl-devel                    # The GNU Scientific Library (GSL) is a collection of routines for numerical analysis, written in C.
			
  		4. Install AMPL:
  
  			cd ~/DECOGO/packages/SCIP/scipoptsuite-7.0.2/scip/interfaces/ampl
  			./get.ASL
  			cd solvers
  			make -f makefile.u
  			cd ..
			mkdir build; cd build
			cmake .. -DSCIP_DIR=~/DECOGO/packages/SCIP/scipoptsuite-7.0.2/build
			make
			ln -s `pwd`/scipampl ~/bin
	
### (Optinal) Build the decogo's documentation:

1. Install the packages:

	conda install graphviz sphinx sphinx_rtd_theme
		
3. Make:

	make html
		
4. Open:

	cd _build/html
	open index.html

