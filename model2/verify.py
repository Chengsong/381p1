import numpy as np
import random

def main():
    random_wr = []
    mid = np.genfromtxt('Middle_pickrate_winrate.csv', delimiter=',')
    mid = mid[:, 1]
    off = np.genfromtxt('Off_pickrate_winrate.csv', delimiter=',')
    off = off[:, 1]
    safe = np.genfromtxt('Safe_pickrate_winrate.csv', delimiter=',')
    safe = safe[:, 1]
    heroes = np.array(range(115))

    for _ in range(1000):
        # choose 2/1/2 or 3/1/1
        if random.random() < 0.5:
            # 2/1/2



if __name__ == '__main__':
    main()