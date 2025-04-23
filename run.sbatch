#!/bin/bash
#
#SBATCH --job-name=cell_count        
#SBATCH --output=logs/count_%j.out   
#SBATCH --error=logs/count_%j.err    
#SBATCH --partition=gpu             
#SBATCH --gres=gpu:1           
#SBATCH --cpus-per-task=8           
#SBATCH --mem=16G                   
#SBATCH --time=05:00:00             
#SBATCH --mail-user=lufany2@illinois.edu
#SBATCH --mail-type=END,FAIL

source /home/a-m/lufany2/miniforge3/etc/profile.d/conda.sh
conda activate t_cell


python ./cell_count.py \
    ./Bile_Acid_BMDM_Images/ \
    --output_csv ./cell_counts.csv \
    --annotate_dir ./annotated_images