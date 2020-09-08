#!/bin/bash

K_FILE="input_K_sample.txt"
UPPER=1
LOWER=-6
PLT_UPPER=0
PLT_LOWER=-4
MAX_LOG_J=1.5
MIN_LOG_J=-0.5
ASPECT=0.8

python 3_plot_spactrum_J_abs.py ${K_FILE} ${UPPER} ${LOWER} ${PLT_UPPER} ${PLT_LOWER} ${MAX_LOG_J} ${MIN_LOG_J} ${ASPECT}
