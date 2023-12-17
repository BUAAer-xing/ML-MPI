#!/bin/bash 
#SBATCH -J mpi-ml-computation_1-814
#SBATCH -p xahcnormal
#SBATCH -N 2
#SBATCH --ntasks-per-node=64
#SBATCH --time 48:00:00
#SBATCH --comment=BASE 
###SBATCH -o std.out.%j
###SBATCH -e std.err.%j
#SBATCH -o /work/home/acjhjlnmhg/congxing/projects/mpi-ml/std/std.out.%j
#SBATCH -e /work/home/acjhjlnmhg/congxing/projects/mpi-ml/std/std.err.%j


### Get parameters from GUI

MIDFILE_DIR=/work/home/acjhjlnmhg/congxing/projects/mpi-ml/.portal
source $MIDFILE_DIR/job_portal.var
source $MIDFILE_DIR/job_interface.var

### Set basic var   ### MARK_slurm2pbs

JOBID=$SLURM_JOB_ID                                  ### slurm2pbs
NP=$SLURM_NPROCS                                     ### slurm2pbs
NNODE=`srun hostname | sort | uniq | wc -l`          ### slurm2pbs

LOG_FILE=$WORK_DIR/job_${JOB_NAME}_${JOBID}.log
HOST_FILE=$WORK_DIR/job_${JOB_NAME}_${JOBID}_${NP}c_${NNODE}n.ma 

srun hostname | sort | uniq -c |awk '{print $2":"$1}' > $HOST_FILE  ### slurm2pbs

### Write basic job infomations

echo -e "The start time is: `date +"%Y-%m-%d %H:%M:%S"` \n" | tee -a $LOG_FILE 
echo -e "My job ID is: $JOBID \n" | tee -a $LOG_FILE  
echo -e "The total cores is: $NP \n" | tee -a $LOG_FILE 
echo -e "The hosts is: \n" | tee -a $LOG_FILE
cat $HOST_FILE | tee -a $LOG_FILE
echo -e "\n"  | tee -a $LOG_FILE 


### Run APP

  # MARK_CMD  #Don't delete this line!!!
#!/bin/bash
## job script created by Gridview Jobmanager.
source ~/miniconda3/etc/profile.d/conda.sh  
conda activate mpi-ml   
conda --version

# Total number of IDs
total_ids=814
# Array of values for x
x_values=(1 2 4 6 8 10 12 16 24 32 48 64 128)
total_x=${#x_values[@]}
# Current progress
current_progress=0

# Loop over ID values from 1 to 2000
for ((id = 1; id < 815; id++))
do
    echo "Sparse Matrix ID: $id"
    # For each ID, loop over the values of x
    for x in "${x_values[@]}"
    do
        # Execute the mpi run command
        mpirun -hosts=$SLURM_NODELIST -n $x python mpi-ml.py $id log_1.txt time_1.csv
        echo -n "progress_size=$x completed ["
        # Print the progress bar
        for ((i=0; i< $total_x; i++))
        do
            if [ $i -lt $((current_progress % total_x)) ]; then
                echo -n "="
            else
                echo -n " "
            fi
        done
        echo "]"
        let current_progress+=1
    done
    # Print the overall progress
    echo "Total Progress: $(($id * 100 / 814 ))%"
done

echo "1-814 tasks completed!"

  # MARK_BASH #Don't delete this line!!!

echo The end time is: `date +"%Y-%m-%d %H:%M:%S"` | tee -a $LOG_FILE   

