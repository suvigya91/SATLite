.. _overview:

********
Overview
********

As a part of SATLite design and development, primary focus is to report the exceptions and errors occured due to inadmissible loading of environment or improper input files on the Supercomputer. The continuous development in the scientific tools and changes in their source code raised a requirement to develop a tool that can report any errors relating to its execution on the remote supercomputers.


Design
======

.. figure:: images/satlite.*
   :width: 450pt
   :align: center
   :alt: EnMD Architecture

   `Figure 1: SATLite tool architecture`

SATLite tool provides a set of explicit APIs to the users to test their own scientific tool. It has been currently tested for Amber, CoCo, Gromacs and LSDMap. The environment loading, file transfer, Job scheduler script generation and its execution is hidden from the users, hence, they can solely focus on the development of scientific tools rather than concentrating less on debugging the errors and exceptions.


Components
==========
The components exposed to the users are discussed below. These components are the parameters that are required to be set using ``set_attribute()``.


Scientific Tool Name
---------------------

This is the field where user has to provide the scientific tool name (currently supported scientific tool name are Amber, CoCo, Gromacs and LSDMap) that has to be tested. For example,

			``name = amber``


Resource Name
---------------
The input to this field is the name of the supercomputer or any target machine where the execution of scientific tool has to be checked. This currently supports SLURM job scheduler. For example,
			
			``resource = xsede.stampede``


Arguments
----------
The list of input files specific to the scientific tools along with the arguments are provided in a specific format as shown in the example below.

			``arguments = ['argument1 = input_file1',``
					``'argument2 = input_file2]``


Exe
----
This is an optional field where users can provide their executable which then overrides the default executable.

User Modules
-------------
This is an optional field where user can explictly provide the environments that are to be required. The in-built modules specific to scientific tools (Amber, CoCO, Gromacs and LSDMap) are used if no user modules are provided.

Run-time
---------
This is recently added optional feature where user can provide an estimate range for run time to check for additional execution failures if no exit code or error is found. The actual run time of the execution is should lie in the runtime range provided by the user. It is provided in the following format:
			``runtime = ["min_time (hh:mm:ss)","max_time (hh:mm:ss)"]`` 


