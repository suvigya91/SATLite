.. _user_guide:

***********
User Guide
***********

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

