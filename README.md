# K2J

K2J converts an optimized interaction matrix _K_ calculated by [PHi-C](https://github.com/soyashinkai/PHi-C) into genome microrheology spectra and consists of Python codes.
The theoretical background and demonstration are described in:

-   Soya Shinkai, Takeshi Sugawara, Hisashi Miura, Ichiro Hiratani, and Shuichi Onami. (2020). **Microrheology for Hi-C Data Reveals the Spectrum of the Dynamic 3D Genome Organization.** [_Biophysical Journal_ **118** 2220–2228](https://doi.org/10.1016/j.bpj.2020.02.020).

-   Soya Shinkai, Shuichi Onami, and Ryuichiro Nakato. (2020). **Toward understanding the dynamic state of 3D genome.** [_Computational and Structural Biotechnology Journal_ **18** 2259–2269](https://doi.org/10.1016/j.csbj.2020.08.014).

## Requirements

K2J codes require the following Python libraries:

-   os
-   sys
-   numpy
-   matplotlib

## Quick Start

Move to the directory [_Tutorial_](/Tutorial):

    cd Tutorial

Then, run the following scripts:

    ./run_1.sh
    ./run_2.sh
    ./run_3.sh
    ./run_4.sh

These scripts generate spectra data in the directory [_data_J_tan_](/Tutorial/data_J_tan) and figures in the directory [_figs_](/Tutorial/figs), although these files have been prepared.
It will take a few minutes to run the first script.
Here, we used an input file of a _K_ matrix for chromosome 6 of mouse ES cells.

## Usage

K2J consists of the following four Python codes:

-   1_calc_J_tan.py
-   2_plot_Js.py
-   3_plot_spactrum_J_abs.py
-   4_plot_spactrum_tan.py

### 1. Calculation of compliances _J'_, _J''_, |_J\*_| and tanδ = _J'_/_J''_ at angular frequencies _ω_

### 2. Plot of microrheology

### 3. Conversion of a sparce matrix format into a dense contact matrix

### 4. Conversion of a sparce matrix format into a dense contact matrix
