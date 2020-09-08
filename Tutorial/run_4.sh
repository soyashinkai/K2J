#!/bin/bash

K_FILE="input_K_sample.txt"
UPPER=1
LOWER=-6
PLT_UPPER=0
PLT_LOWER=-4
MAX_LOG_tan=0.2
ASPECT=0.8

python 4_plot_spactrum_tan.py ${K_FILE} ${UPPER} ${LOWER} ${PLT_UPPER} ${PLT_LOWER} ${MAX_LOG_tan} ${ASPECT}
