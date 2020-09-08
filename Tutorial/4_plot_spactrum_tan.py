import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import os
# --------------------------------------------------------------------------------------------------
# Set command line arguments
argv = sys.argv
argc = len(argv)
if (argc != 6):
    print("Usage: python " + argv[0] + " K_FILE UPPER LOWER")
    exit()
K_FILE = argv[1]
UPPER = int(argv[2])
LOWER = int(argv[3])
PLT_UPPER = int(argv[4])
PLT_LOWER = int(argv[5])
# --------------------------------------------------------------------------------------------------
MAX_LOG_tan = 0.2
MIN_LOG_tan = -0.2
ASPECT = 0.8
K = np.loadtxt(K_FILE)
N = K.shape[0]
M = 100 * (UPPER - LOWER)
START = 100 * (PLT_LOWER - LOWER)
END = 100 * (PLT_UPPER - LOWER) + 1
DIR = "data_J_tan"
os.makedirs("figs", exist_ok=True)
FILE_FIG = "figs/spectrum_tan.svg"
YTICKS_LABELS = []
for n in range(PLT_LOWER, PLT_UPPER + 1):
    YTICKS_LABELS.append(n)
# --------------------------------------------------------------------------------------------------


def main():
    # ----------------------------------------------------------------------------------------------
    tan = np.zeros((M + 1, N))
    for n in range(N):
        FILE_READ = DIR + "/J_tan_n{0:d}.txt".format(n)
        data = np.loadtxt(FILE_READ)
        tan[:, n] = data[:, 4]
    # ----------------------------------------------------------------------------------------------
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 24
    # ----------------------------------------------------------------------------------------------
    plt.figure(figsize=(8, 4))
    plt.ylabel(r"$\mathrm{\mathbf{log_{10} \bar{\omega}}}$")
    plt.yticks(np.arange(0, END - START, 100), YTICKS_LABELS)

    plt.imshow(np.log10(tan[START:END, :]),
               cmap="coolwarm",
               clim=(MIN_LOG_tan, MAX_LOG_tan),
               aspect=ASPECT,
               origin="lower")
    plt.colorbar(shrink=0.8,  # orientation="horizontal",
                 label=r"$\mathrm{\mathbf{log_{10} \mathbf{tan δ(\bar{\omega})}}}$",
                 ticks=[MIN_LOG_tan, 0, MAX_LOG_tan])

    ax = plt.gca()
    ax.spines["right"].set_color("none")  # 右枠消し
    ax.spines["top"].set_color("none")    # 上枠消し
    ax.spines["bottom"].set_color("none")    # 下枠消し
    plt.tick_params(labelbottom=0, bottom=0, labelleft=1)

    plt.savefig(FILE_FIG)
    plt.close()
# --------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
