#!/bin/bash
source ~/.bashrc
cd /scratch/asharma/siv_viv/q4_2023/utilities
condaEnv
conda activate /projects/exawind/ganeshv/conda/analysis
cd /home/asharma/python-toolbox
python -m pip install -e .
cd /scratch/asharma/siv_viv/q4_2023/utilities
python gen_cases.py
 
