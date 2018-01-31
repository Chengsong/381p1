# Wendong Cui
# verify the model3 by randomly selecting 2 teams and
# calculating the win rate difference
import numpy as np
import random as rd

n = 115  # the number of heroes


def main():
    wr_diffs = []
    sample = range(0, n)
    raw_wr = np.load('../hero_matchup_grid.npy')   # win rate of each hero to other heroes
    wr = np.zeros(shape=[115], dtype=float)     # the actual win rate of each hero
    for i in range(0, n):
        wr[i] = np.mean(raw_wr[i])

    best_hrs = [15, 64, 81, 101, 114, 14, 19, 87, 104, 113]
    opt_wr_diff = 0
    for j in range(0, 5):
        opt_wr_diff += wr[best_hrs[j]]
    for j in range(5, 10):
        opt_wr_diff -= wr[best_hrs[j]]
    wr_diffs.append(opt_wr_diff)
    print(opt_wr_diff)
"""
    for i in range(0, 1000):
        hrs = rd.sample(sample, 10)
        wr_diff = 0
        for j in range(0, 5):
            wr_diff += wr[hrs[j]]
        for j in range(5, 10):
            wr_diff -= wr[hrs[j]]
        wr_diff = abs(wr_diff)
        wr_diffs.append(wr_diff)

    np.savetxt("verify.csv", wr_diffs, delimiter=",")
"""

if __name__ == '__main__':
    main()

