#!/bin/bash

K_FILE="input_K_sample.txt"
UPPER=1
LOWER=-6
PLT_UPPER=0
PLT_LOWER=-4

python 3_plot_spactrum_J_abs.py ${K_FILE} ${UPPER} ${LOWER} ${PLT_UPPER} ${PLT_LOWER}
