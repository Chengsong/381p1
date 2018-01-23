import urllib.request
import time


hero_html_fmt = 'C:\\Users\\fired\\PycharmProjects\\DotALP\\hero_data_html\\{}.html'

# The following link has winrates
wr_url = "https://www.dotabuff.com/heroes/winning"
# The following link has economy stats
ec_url = "https://www.dotabuff.com/heroes/economy"
# The following link has times played
pl_url = "https://www.dotabuff.com/heroes/played"


# We can scrape this to give us winrate of each of the heroes.

# At any link of the following type, for each of the heroes,
# there is the advantage/disadvantage value against any particular hero
#
# Hero names, if they have spaces, are hyphenated
"https://www.dotabuff.com/heroes/zeus/matchups" # for example

hero_names = "heroes.txt" # turn this into dictionary/numpy array/list
with open(hero_names) as f:
    heroes = f.read().split("\n")

TOTAL_HERO_NUMBER = len(heroes)

if False: # So we don't download again, temp fix
    for i, hero in enumerate(heroes):
        hero_matchup_url = "https://www.dotabuff.com/heroes/{}/matchups".format(hero.lower())

        page_request = urllib.request.Request(hero_matchup_url)
        page_request.add_header('User-agent', "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
        response = urllib.request.urlopen(page_request)
        webContent = response.read()

        f = open(hero_html_fmt.format(hero), 'wb')
        f.write(webContent)
        f.close()

        print(i/TOTAL_HERO_NUMBER)
        time.sleep(1)

# other useful links
for link in [wr_url, ec_url, pl_url]:
    page_request = urllib.request.Request(link)
    page_request.add_header('User-agent', "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
    response = urllib.request.urlopen(page_request)
    webContent = response.read()

    f = open("C:\\Users\\fired\\PycharmProjects\\DotALP\\game_data\\{}.html".format(link.split("/")[-1]), 'wb')
    f.write(webContent)
    f.close()

    time.sleep(1)

# We can scrape this to give us:
#   1. "Advantages" which is a proprietary dotabuff rating
#   2. Individual winrates
#   3. Number of matches played (Not useful?)

#np.save("hero_matchup_grid", hero_matchup_grid)
