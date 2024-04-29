import re
import requests
from bs4 import BeautifulSoup

class TeamInfo (object):
    name = ""
    url = ""

    def __init__(self, name, url):
        self.name = name
        self.url = url

URL = "https://www.hna.com/leagues/standings.cfm?leagueID=5761&clientID=2296"
URLPrefix = "https://www.hna.com/leagues/"
standingsPage = requests.get(URL)

standingsPageSoup = BeautifulSoup(standingsPage.content, "html.parser")

# Gets the whole team page URL for every team
teamStandingsPage = standingsPageSoup.find_all('a', {'href':re.compile("stats_1team.cfm")})

teams = []

for team in teamStandingsPage:
    teams.append(TeamInfo(team.find("span").text, URLPrefix + team['href']))

for teamPage in teams:
    # Get head to head info
    teamPage = requests.get(teamPage.url)
    teamSoupPage = BeautifulSoup(teamPage.content, "html.parser")

    # Get players above 1 ppg