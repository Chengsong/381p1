import numpy as np
import bs4

game_data_dr  = "C:\\Users\\fired\\PycharmProjects\\DotALP\\game_data\\"
hero_data_dr  = "C:\\Users\\fired\\PycharmProjects\\DotALP\\hero_data_html\\"
hero_names    = "heroes.txt"
full_names    = "heroes_stylized.txt"
game_data_fmt = "C:\\Users\\fired\\PycharmProjects\\DotALP\\game_data\\{}.html"
hero_html_fmt = "C:\\Users\\fired\\PycharmProjects\\DotALP\\hero_data_html\\{}.html"


with open(hero_names) as f:
    heroes = f.read().split("\n")

with open(full_names) as f:
    full_name_heroes = f.read().split("\n")

TOTAL_HERO_NUMBER = len(heroes)

def save_grid():
    # Parsing hero advantage from scraped files
    hero_name_column = 0
    win_rate_column  = 3

    hero_grid = {}

    for hero, full_name in zip(heroes, full_name_heroes):
        hero_grid[full_name] = {}

        with open(hero_html_fmt.format(hero.lower()), encoding="utf8") as hero_data:
            soup = bs4.BeautifulSoup(hero_data.read() , 'html.parser')

        tagged_tr = soup.find_all('tr')

        for tag in tagged_tr:
            td = tag.find_all('td')

            if len(td) > 0 and td[0]["class"][0] == "cell-icon":
                name_line = td[hero_name_column]
                adv_line  = td[win_rate_column]

                hero_name = name_line["data-value"]
                winrate = float(adv_line["data-value"])

                hero_grid[full_name][hero_name] = winrate

                #print("{} wins against {} {}% of the time.".format(hero, hero_name, winrate))

    hero_grid_matrix = np.zeros([TOTAL_HERO_NUMBER, TOTAL_HERO_NUMBER])

    for i, hero_i in enumerate(full_name_heroes):
        winrates = hero_grid[hero_i]
        for j, hero_j in enumerate(full_name_heroes):
            if i is not j:
                winrate_i_vs_j = winrates[hero_j]
            else:
                winrate_i_vs_j = 0.0 #50.0 maybe?


            hero_grid_matrix[i,j] = winrate_i_vs_j

    #print(hero_grid_matrix)
    np.save("hero_matchup_grid",hero_grid_matrix)

def save_xpm_gpm():
    hero_name_column = 0
    gpm_column = 2
    xpm_column = 3

    hero_gpm_xpm_dict = {}

    with open(game_data_fmt.format("economy"), encoding="utf8") as hero_data:
        soup = bs4.BeautifulSoup(hero_data.read(), 'html.parser')

    #print(soup.prettify())
    tagged_tr = soup.find_all('tr')
    for tag in tagged_tr:
        tags_td = tag.find_all('td')

        if len(tags_td) > 0:
            name = tags_td[hero_name_column]["data-value"]
            gpm = tags_td[gpm_column]["data-value"]
            xpm = tags_td[xpm_column]["data-value"]

            hero_gpm_xpm_dict[name] = (float(gpm), float(xpm))

            #print("{} has {} gpm and {} xpm.".format(name, gpm, xpm))

    hero_gpm_xpm = np.zeros([2, TOTAL_HERO_NUMBER])
    for i, hero in enumerate(full_name_heroes):
        hero_gpm_xpm[..., i] = hero_gpm_xpm_dict[hero]

    np.save("hero_gpm_xpm", hero_gpm_xpm)

#save_grid()
#save_xpm_gpm()