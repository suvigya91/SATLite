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
                    #runtime = ["0:0:1","0:0:15"]
                    )
    test.run()

















##                      #coco
##                      arguments = ['--grid=5',
##                                   '--dims=3',
##                                   '--frontpoints=4',
##                                   '--topfile=/home/suvigya/inp/penta.top',
##                                   '--mdfile=/home/suvigya/inp/*.ncdf',
##                                   '--mpi','--selection=protein']

##                      #gromacs
##                      arguments = ['/home/suvigya/inp/run.py',
##                                   '--mdp=/home/suvigya/inp/grompp.mdp',
##                                   '--gro=/home/suvigya/inp/start.gro',
##                                   '--top=/home/suvigya/inp/topol.top']

                      #lsdmap
##                      arguments = ['-f=/home/suvigya/inp/config.ini',
##                                   '-w=/home/suvigya/inp/weight.w',
##                                   '-c=/home/suvigya/inp/tmp.gro',
##                                   '-n=/home/suvigya/inp/out.nn']

    #test.dispFile()
