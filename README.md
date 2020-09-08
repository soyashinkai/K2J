# K2J

K2J converts an optimized interaction matrix _K_ calculated by [PHi-C](https://github.com/soyashinkai/PHi-C) into genome microrheology spectra and consists of Python codes.

![overview](/images/overview.png)

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

### 1. Calculation of compliances _J'_, _J''_, | _J\*_ = _J'_ + _i J''_ | and tanδ = _J'_ / _J''_ at angular frequencies _ω_

    python 1_calc_J_tan.py K_FILE UPPER LOWER

The command converts the input _K_ matrix data into the values of comliances _J'_, _J''_, | _J\*_ = _J'_ + _i J''_ | and tanδ = _J'_ / _J''_ at angular frequencies 10<sup>LOWER</sup> &lt;= _ω_ &lt;= 10<sup>UPPER</sup>.
The output files named _J_tan_n{INDEX}.txt_ are stored in the newly made directory _data_J_tan_, where 0 &lt;= INDEX &lt; _N_.

-   K_FILE: the file name of an input _K_ matrix (_N_ x _N_ size),
-   UPPER: the exponent of the upper angular freqeuncy _ω_ = 10<sup>UPPER</sup>,
-   LOWER: the exponent of the lower angular freqeuncy _ω_ = 10<sup>LOWER</sup>.

### 2. Plot of _J'_ and _J''_ curves to the angular frequncy _ω_

    python 2_plot_Js.py K_FILE UPPER LOWER

The command plots _J'_ and _J''_ curves to the angular frequncy _ω_.
The output file named _Js.png_ is stored in the newly made directory _figs_.

-   K_FILE: the file name of an input _K_ matrix (_N_ x _N_ size),
-   UPPER: the exponent of the upper angular freqeuncy _ω_ = 10<sup>UPPER</sup>,
-   LOWER: the exponent of the lower angular freqeuncy _ω_ = 10<sup>LOWER</sup>.

### 3. Plot of | _J\*_ | spectrum

    python 3_plot_spactrum_J_abs.py K_FILE UPPER LOWER PLT_UPPER PLT_LOWER MAX_LOG_J MIN_LOG_J ASPECT

The command plots the | _J\*_ | spectrum to the angular frequncy _ω_.
The output file named _spectrum_J_abs.svg_ is stored in the directory _figs_.

-   K_FILE: the file name of an input _K_ matrix (_N_ x _N_ size),
-   UPPER: the exponent of the upper angular freqeuncy _ω_ = 10<sup>UPPER</sup>,
-   LOWER: the exponent of the lower angular freqeuncy _ω_ = 10<sup>LOWER</sup>,
-   PLT_UPPER: the exponent of the upper angular freqeuncy _ω_ = 10<sup>PLT_UPPER</sup> in the spectrum,
-   PLT_LOWER: the exponent of the lower angular freqeuncy _ω_ = 10<sup>PLT_LOWER</sup> in the spectrum,
-   MAX_LOG_J: the upper value of | _J\*_ | in the heatmap,
-   MIN_LOG_J: the lower value of | _J\*_ | in the heatmap,
-   ASPECT: the aspect ratio of the spectrum.

### 4. Plot of tanδ spectrum

    python 4_plot_spactrum_tan.py K_FILE UPPER LOWER PLT_UPPER PLT_LOWER MAX_LOG_tan ASPECT

The command plots the tanδ spectrum to the angular frequncy _ω_.
The output file named _spectrum_tan.svg_ is stored in the directory _figs_.

-   K_FILE: the file name of an input _K_ matrix (_N_ x _N_ size),
-   UPPER: the exponent of the upper angular freqeuncy _ω_ = 10<sup>UPPER</sup>,
-   LOWER: the exponent of the lower angular freqeuncy _ω_ = 10<sup>LOWER</sup>,
-   PLT_UPPER: the exponent of the upper angular freqeuncy _ω_ = 10<sup>PLT_UPPER</sup> in the spectrum,
-   PLT_LOWER: the exponent of the lower angular freqeuncy _ω_ = 10<sup>PLT_LOWER</sup> in the spectrum,
-   MAX_LOG_tan: the upper value of tanδ in the heatmap,
-   ASPECT: the aspect ratio of the spectrum.
