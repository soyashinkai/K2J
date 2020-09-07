import numpy as np
import sys
import os
# --------------------------------------------------------------------------------------------------
# Set command line arguments
argv = sys.argv
argc = len(argv)
if (argc != 4):
    print("Usage: python " + argv[0] + " K_FILE UPPER LOWER")
    exit()
FILE_READ = argv[1]
UPPER = int(argv[2]) # the exponent of the upper ω
LOWER = int(argv[3]) # the exponent of the lower ω
# --------------------------------------------------------------------------------------------------
M = 100 * (UPPER - LOWER)
DIR = "data_J_tan"
os.makedirs(DIR, exist_ok=True)
# --------------------------------------------------------------------------------------------------


def Read_K():
    K = np.loadtxt(FILE_READ)
    N = K.shape[0]
    return K, N
# --------------------------------------------------------------------------------------------------


def Transform_K_into_L(K):
    d = np.sum(K, axis=0)
    D = np.diag(d)
    L = D - K
    return L
# --------------------------------------------------------------------------------------------------


def main():
    K, N = Read_K()
    # ----------------------------------------------------------------------------------------------
    L = Transform_K_into_L(K)
    lam, Q = np.linalg.eigh(L)
    # ----------------------------------------------------------------------------------------------
    for n in range(N):
        data = np.zeros((M + 1, 5))
        for m in range(M + 1):
            # --------------------------------------------------------------------------------------
            omega = 10**(0.01 * (m + LOWER * 100))
            data[m, 0] = omega
            # --------------------------------------------------------------------------------------
            for p in range(1, N):
                data[m, 1] += Q[n, p] * Q[n, p] * 3 * lam[p] / (omega * omega + 9 * lam[p] * lam[p])
                data[m, 2] += Q[n, p] * Q[n, p] * omega / (omega * omega + 9 * lam[p] * lam[p])
            # --------------------------------------------------------------------------------------
            J2 = data[m, 1] * data[m, 1] + data[m, 2] * data[m, 2]
            data[m, 3] = np.sqrt(J2)
            data[m, 4] = data[m, 2] / data[m, 1]
        # ------------------------------------------------------------------------------------------
        FILE_OUT = DIR + "/J_tan_n{0:d}.txt".format(n)
        np.savetxt(FILE_OUT, data, fmt="%e")
# --------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
