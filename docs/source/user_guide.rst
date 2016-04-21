.. _user_guide:

***********
User Guide
***********

Execution
==========

There are two ways for the users to execute the SATLite, namely:
	1. Command Line Tool
	2. Use the exposed APIs in the code.

Command Line Tool
------------------
To run SATLite using command line tool, users are required to provide scientific tool name, target remote machine and arguments file or a file with the list of input files that are required for the execution of the scientific tool. Users can also provide optional executable name and module file explicitly. They can also provide optional execution runtime range. It is recommended to provide a runtime range so as to enhance the failure reporting. The resulting invocation of SATLite should be:

.. parsed-literal::
	python satlite_exe.py --name <scientific_tool_name> --resource <target_resource_name> --arguments <argument_file> --exe <Optional_executable> --modules <optional_module_file> --runtime <Optional_runtime_range>


Where,

.. parsed-literal::
	scientific_tool_name = Scientific Tools (Amber, CoCo, Gromacs, LSDMap)
	target_resource_name = Remote Supercomputer Name (Currently tested on Stampede)
	argument_file	     = File of list of input files with arguments
	Optional_executable  = Executable
	optional_module_file = File with list of modules
	Optional_runtime_range= Runtime range in format [min_time, max_time] in hh:mm:ss


Use the exposed APIs in the code
---------------------------------
This section provides a guide for using the APIs exposed to the users. The below mentioned example executes Amber on Stampede.

.. code-block:: python
   

   """
   Sample Code
   """
   from satlite import SATLite


   if __name__ == "__main__":
   	test = SATLite()
   	test.set_attribute(name = 'amber',
                           
                          resource = 'xsede.stampede',
                      
                          #amber
                          arguments = ['-O',
                                 '-i=/home/suvigya/inp/min.in',
                                 '-p=/home/suvigya/inp/penta.top',
                                 '-c=/home/suvigya/inp/penta.crd',
                                 '-inf=/home/suvigya/inp/min.inf',
                                 '-r=/home/suvigya/inp/md.crd',
                                 '-ref=/home/suvigya/inp/min.crd'],

                         #Executable optional
                         # exe = sander
                       
                         #amber modules optional
                         modules = ["module load TACC",
                               "module load intel/13.0.2.146",
                               "module load python/2.7.9",
                               "module load netcdf/4.3.2",
                               "module load hdf5/1.8.13"]
                        runtime = ["0:0:1","0:0:15"]
                    )
   	test.run()

