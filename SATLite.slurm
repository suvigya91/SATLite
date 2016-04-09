#!/bin/sh

#BATCH -J SATLite
#SBATCH -o /home1/03894/tg831932/SATLite/Output/SATLite.out
#SBATCH -e /home1/03894/tg831932/SATLite/Output/STDERR
#SBATCH -n 1
#SBATCH -p development
#SBATCH -t 00:10:00
#SBATCH --mail-user=suvigya91@gmail.com
#SBATCH --mail-type=begin
#SBATCH --mail-type=end


### amber testing ###

## ENVIRONMENT

## EXEC
module load TACC
module load intel/13.0.2.146
module load python/2.7.9
module load netcdf/4.3.2
module load hdf5/1.8.13


ibrun /opt/apps/intel13/mvapich2_1_9/amber/12.0/bin/sander -O -i ${HOME}/SATLite/user_files/min.in -p ${HOME}/SATLite/user_files/penta.top -c ${HOME}/SATLite/user_files/penta.crd -inf ${HOME}/SATLite/user_files/min.inf -r ${HOME}/SATLite/user_files/md.crd -ref ${HOME}/SATLite/user_files/min.crd -o ${HOME}/SATLite/Output/min.out 