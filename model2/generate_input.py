import numpy as np

M = 3 # 0 = MID, 1 = OFF, 2 = SAFE
N = 115

def main():
    # load data
    mid = np.genfromtxt('Middle_pickrate_winrate.csv', delimiter=',')
    mid[0][0] = 0
    off = np.genfromtxt('Off_pickrate_winrate.csv', delimiter=',')
    off[0][0] = 0.5999
    safe = np.genfromtxt('Safe_pickrate_winrate.csv', delimiter=',')
    safe[0][0] = 0.3123
    data = [mid, off, safe]

    with open('model2.lp', 'w') as file:
        # objective function
        terms = []
        for i in range(N):
            for j in range(M):
                terms.append("{}x_{}_{}".format(data[j][i][1], i, j))
        file.write("max: {};\n".format(' + '.join(terms)))

        # constraint 1
        xs = ["x_{}_{}".format(i, j) for j in range(M) for i in range(N)]
        file.write("{} = 5;\n".format(' + '.join(xs)))

        # constraint 2
        for i in range(N):
            xs = ["x_{}_{}".format(i, j) for j in range(M)]
            file.write("{} <= 1;\n".format(' + '.join(xs)))

        # constraint 3
        xs = ["x_{}_{}".format(i, 0) for i in range(N)]
        file.write("{} = 1;\n".format(' + '.join(xs)))
        xs = ["x_{}_{}".format(i, 1) for i in range(N)]
        file.write("1 <= {} <= 2;\n".format(' + '.join(xs)))
        xs = ["x_{}_{}".format(i, 2) for i in range(N)]
        file.write("2 <= {} <= 3;\n".format(' + '.join(xs)))

        # binary variable declaration
        xs = ["x_{}_{}".format(i, j) for j in range(M) for i in range(N)]

        # save to file
        file.write("bin {};\n".format(', '.join(xs)))

if __name__ == '__main__':
    main()