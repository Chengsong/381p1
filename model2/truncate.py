def main():
    with open('model2.out', 'r') as input:
        with open('model2_truncated.out', 'w') as output:
            for line in input.readlines():
                if (not line.startswith('x') or line.endswith('1\n')):
                    output.write(line)

    with open('../heroes_stylized.txt') as input:
        heroes = [hero.strip() for hero in input.readlines()]
    lanes = ['mid', 'off', 'safe']
    with open('model2_truncated.out', 'r') as input:
        with open('result.txt', 'w') as output:
            for line in input.readlines():
                if (line.endswith('1\n')):
                    variable = line.split(' ')[0].split('_')
                    hero = heroes[int(variable[1])]
                    lane = lanes[int(variable[2])]
                    output.write("Hero: {}, Lane: {}\n".format(hero, lane))

if __name__ == '__main__':
    main()