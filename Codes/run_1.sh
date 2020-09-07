#!/bin/bash

K_FILE="input_K_sample.txt"
UPPER=1
LOWER=-6

python 1_calc_J_tan.py ${K_FILE} ${UPPER} ${LOWER}
