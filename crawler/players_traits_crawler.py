from bs4 import BeautifulSoup
import requests
import json

class PlayersCrawler:
	url: str = "https://www.mykhel.com/football/fifa-world-cup-2022-squads-l4/"

	def __init__(self): return

	def get_teams_links(self) -> list:
		print("Getting team links...")

		page = requests.get(PlayersCrawler.url)

		soup = BeautifulSoup(page.content, "html.parser")
	
		teams_div = soup.find("div", { "class": "os-fifateams" })

		teams_blocks = teams_div.find_all("div", {"class" : "os-fifateams-block"})

		links = []
		for team_block in teams_blocks:
			div_tag = team_block.find("div", {"class" : "os-more"})
			a_tag = div_tag.find("a", {"class": "os-more-b"})
			links.append(a_tag['href'])

		return links


	def get_teams_info(self, team_link) -> list:
		print("Getting teams informations...")

		url: str = "https://www.mykhel.com" + team_link

		page = requests.get(url)

		soup = BeautifulSoup(page.content, "html.parser")
		
		team_div = soup.find("div", {"class" : "os-fifacontainer"})

		player_list_div = team_div.find("div", {"class": "os-fifa-playerlist"})

		players_list = player_list_div.find("ul", {"class": "clearfix"}).find_all("li")

		players_page_links = []
		for player in players_list:
			div_tag = player.find("div", {"class" : "playerinfo-viewprofile"})
			a_tag = div_tag.find("a", {"class": "os-more-b"})
			players_page_links.append(a_tag['href'])

		return players_page_links


	def get_player_info(self, player_link, j:int):

		url: str = "https://www.mykhel.com" + player_link

		player_info = {}

		page = requests.get(url)

		soup = BeautifulSoup(page.content, "html.parser")

		content_div = soup.find("div", {"class" : "os-c-ln-main-lt"})

		player_div = content_div.find("div", {"class" : "os-fifacontainer"})
		
		player_details = player_div.find("div", {"class" : "os-profile-details"})
		
		player_info['name'] = player_details.find("div", {"class" : "os-profile-name"}).text
		
		player_informations = player_details.find("ul", {"class" : "clearfix"}).find_all("li")
		player_info['birth'] = player_informations[0].text.split()[3]
		player_info['club'] = player_informations[1].text.split()[1]
		print(f"Getting {j} player from {player_info['club']}")
		player_info['joined_date'] = player_informations[2].text.split()[2]
		player_info['place_of_birth'] = player_informations[3].text.split()[3]
		player_info['number'] = player_informations[4].text.split()[2]
		player_info['height'] = player_informations[5].text.split()[1]
		player_info['weight'] = player_informations[6].text.split()[1]
		player_info['position'] = player_informations[7].text.split()[1]
		
		return player_info



if __name__ == "__main__":

	engine = PlayersCrawler()

	links = engine.get_teams_links()

	players_sticks = []
	
	for i in range(len(links)):
		players_links = engine.get_teams_info(links[i])

		for j in range(len(players_links)):
			players_sticks.append(engine.get_player_info(players_links[j], j))


	with open("players.json", "w") as file:
		file.write(json.dumps(players_sticks))
