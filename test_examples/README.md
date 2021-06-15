## Fedora

It works with system instalation:

	root$> dnf install mpich mpich-devel
	root$> dnf install python3-mpi4py-mpich.x86_64
	root$> dnf install mpi4py-docs.noarch

Docs in `/usr/share/doc/mpi4py-docs`

Put on `/etc/bashrc`:

	$> module load mpi/mpich-x86_64

It sets all variables.

I could not install it with pip3.

