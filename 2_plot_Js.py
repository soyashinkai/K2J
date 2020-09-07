import numpy as np
import matplotlib.pyplot as plt
import sys
# --------------------------------------------------------------------------------------------------
# Set command line arguments
argv = sys.argv
argc = len(argv)
if (argc != 4):
    print("Usage: python " + argv[0] + " K_FILE UPPER LOWER")
    exit()
K_FILE = argv[1]
UPPER = int(argv[2])  # the exponent of the upper ω
LOWER = int(argv[3])  # the exponent of the lower ω
# --------------------------------------------------------------------------------------------------
K = np.loadtxt(K_FILE)
N = K.shape[0]
DIR = "data_J_tan"
FILE_FIG = "fig_Js.png"
# --------------------------------------------------------------------------------------------------


def main():
    # ----------------------------------------------------------------------------------------------
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["font.size"] = 36
    # ----------------------------------------------------------------------------------------------
    plt.figure(figsize=(12, 9))
    plt.xscale("log")
    plt.yscale("log")
    plt.xlim(10**(LOWER), 10**(UPPER))
    plt.ylim(1e-2, 1e3)
    plt.xlabel(r"$\mathrm{\mathbf{\bar{\omega}}}$")
    plt.ylabel(r"$\mathrm{\mathbf{Normalized\ compliance}}$")

    for n in range(N):
        FILE_READ = DIR + "/J_tan_n{0:d}.txt".format(n)
        data = np.loadtxt(FILE_READ)
        plt.plot(data[:, 0], data[:, 1], linewidth=1, color="blue", alpha=0.1)
        plt.plot(data[:, 0], data[:, 2], linewidth=1, color="red", alpha=0.1)

    plt.annotate(r"$\mathrm{\mathbf{\bar{J}'(\bar{\omega})\ (storage)}}$",
                 (0.005, 500), color="blue")
    plt.annotate(r"$\mathrm{\mathbf{\bar{J}''(\bar{\omega})\ (loss)}}$",
                 (0.005, 100), color="red")

    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().yaxis.set_ticks_position("left")
    plt.gca().xaxis.set_ticks_position("bottom")

    plt.tight_layout()
    plt.savefig(FILE_FIG)
    plt.close()
# --------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
