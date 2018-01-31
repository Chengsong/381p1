# Wendong Cui
# the python script to generate a ".txt" input file for
# project1 model3, the most interesting match in the game
import numpy as np

n = 115  # the number of heroes


def main():
    # firstly, validate and preprocess data
    raw_wr = np.load('hero_matchup_grid.npy')   # win rate of each hero to other heroes
    gpm = np.load('hero_gpm_xpm.npy')[0]        # gold per minute for each hero
    epm = np.load('hero_gpm_xpm.npy')[1]        # exp per minute for each hero
    total_gpm = np.mean(gpm) * 5
    total_epm = np.mean(epm) * 5
    wr = np.zeros(shape=[115], dtype=float)     # the actual win rate of each hero
    for i in range(0, n):
        wr[i] = np.mean(raw_wr[i])

    # open the input file
    f = open("input.txt", "w")
    # print the objective function
    f.write("max:")
    for i in range(1, n+1):
        f.write("+" + str(wr[i - 1]) + "y" + str(i))
    f.write(";\n")

    # print constraint 1, team1 > team2
    for i in range(1, n+1):
        f.write("+" + str(wr[i - 1]) + "x" + str(i))
    f.write(" > ")
    for i in range(1, n+1):
        f.write("+" + str(wr[i - 1]) + "y" + str(i))
    f.write(";\n")

    # print constraint 2, hero can only be picked once
    for i in range(1, n+1):
        f.write("y" + str(i) + " + x" + str(i) + "<= 1;\n")

    # print constraint 3, each team must have 5 heroes
    for i in range(1, n+1):
        f.write("+y" + str(i))
    f.write(" = 5;\n")
    for i in range(1, n+1):
        f.write("+x" + str(i))
    f.write(" = 5;\n")

    # print constraint 4, each team's total revenue must be limited
    for i in range(1, n+1):
        f.write("+" + str(gpm[i - 1]) + "y" + str(i))
    f.write(" <= " + str(total_gpm) + ";\n")
    for i in range(1, n+1):
        f.write("+" + str(epm[i - 1]) + "y" + str(i))
    f.write(" <= " + str(total_epm) + ";\n")
    for i in range(1, n+1):
        f.write("+" + str(gpm[i - 1]) + "x" + str(i))
    f.write(" <= " + str(total_gpm) + ";\n")
    for i in range(1, n+1):
        f.write("+" + str(epm[i - 1]) + "y" + str(i))
    f.write(" <= " + str(total_epm) + ";\n")

    # print constrain 4, all binary variables
    f.write("bin ")
    for i in range(1, n):
        f.write("y" + str(i) + ", x" + str(i) + ", ")
    f.write("y115, x115;\n")
    f.close()


if __name__ == '__main__':
    main()

