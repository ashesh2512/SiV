#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=48:00:00
#SBATCH --array=0-1
#SBATCH --account=sviv
#SBATCH --qos=high
#SBATCH --job-name=IEA15MW_SIV_VIV
#SBATCH --output=out.%x_%j
#SBATCH --mail-user=ashesh.sharma@nrel.gov
#SBATCH --mail-type=BEGIN,END,FAIL

export SPACK_MANAGER=/home/asharma/exawind_spack_latest/spack-manager
source ${SPACK_MANAGER}/configs/eagle/env.sh
module load mpt
source ${SPACK_MANAGER}/start.sh && quick-activate ${SPACK_MANAGER}/environments/openfast_only
spack load openfast
openfast_exec="$(spack location -i openfast)/bin/openfast"

caselist=$(printf "cases_%02d" ${SLURM_ARRAY_TASK_ID}) 

for i in `cat ${caselist}`
do
    cd $i
    ${openfast_exec} *fst &> sim_log &
    cd -
done

wait
