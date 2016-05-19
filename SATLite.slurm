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


### lsdmap testing ###

## ENVIRONMENT
export PYTHONPATH=/home1/03036/jp43/.local/lib/python2.7/site-packages
export PATH=/home1/03036/jp43/.local/bin:$PATH

## EXEC
module load TACC
module load -intel +intel/14.0.1.106
module load python/2.7.6


 lsdmap -f ${HOME}/SATLite/user_files/config.ini -w ${HOME}/SATLite/user_files/weight.w -c ${HOME}/SATLite/user_files/tmp.gro -n ${HOME}/SATLite/user_files/out.nn 
