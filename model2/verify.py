import numpy as np
import random
import matplotlib.pylab as plt

HEROES = np.array(range(115))

def random_winrate(arr, n):
    return sum(arr[np.random.choice(a=HEROES[arr[:] > 0], size=n, replace=False)])

def main():
    random_wr = []
    mid = np.genfromtxt('Middle_pickrate_winrate.csv', delimiter=',')
    mid = mid[:, 1]
    off = np.genfromtxt('Off_pickrate_winrate.csv', delimiter=',')
    off = off[:, 1]
    safe = np.genfromtxt('Safe_pickrate_winrate.csv', delimiter=',')
    safe = safe[:, 1]


    for _ in range(1000):
        wr = 0
        # choose 2/1/2 or 3/1/1
        if random.random() < 0.5:
            # 2/1/2
            wr += random_winrate(mid, 1)
            wr += random_winrate(off, 2)
            wr += random_winrate(safe, 2)
        else:
            # 3/1/1
            wr += random_winrate(mid, 1)
            wr += random_winrate(off, 1)
            wr += random_winrate(safe, 3)
        wr /= 5
        random_wr.append(wr)

    plt.hist(random_wr, bins=100)
    plt.axvline(x=.57178, color='r')
    plt.xlabel('winrate')
    plt.ylabel('frequency')
    plt.title('Histogram of winrates of 1000 random teams')
    plt.show()


if __name__ == '__main__':
    main()