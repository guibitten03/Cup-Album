from bs4 import BeautifulSoup
import requests

class PlayersCrawler:
	url: str = "https://www.mykhel.com/football/fifa-world-cup-2022-squads-l4/"

	def __init__(self): return

	def get_teams_links(self) -> list:
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
		url: str = "https://www.mykhel.com" + team_link

		page = requests.get(url)

		soup = BeautifulSoup(page.content, "html.parser")
		
		team_div = soup.find("div", {"class" : "os-fifacontainer"})
	
		team_title = team_div.find("h1").text.split()[0]

		player_list_div = team_div.find("div", {"class": "os-fifa-playerlist"})

		players_list = player_list_div.find("ul", {"class": "clearfix"}).find_all("li")

		players_page_links = []
		for player in players_list:
			div_tag = player.find("div", {"class" : "playerinfo-viewprofile"})
			a_tag = div_tag.find("a", {"class": "os-more-b"})
			players_page_links.append(a_tag['href'])

		return players_page_links, team_title

	def get_player_info(self, player_link, team_title):
		url: str = "https://www.mykhel.com" + player_link

		player_info = {}

		page = requests.get(url)

		soup = BeautifulSoup(page.content, "html.parser")

		content_div = soup.find("div", {"class" : "os-c-ln-main-lt"})

		player_div = content_div.find("div", {"class" : "os-fifacontainer"})
		
		player_details = player_div.find("div", {"class" : "os-profile-details"})
		
		player_info['title'] = team_title
		player_info['name'] = player_details.find("div", {"class" : "os-profile-name"}).text
		
		player_informations = player_details.find("ul", {"class" : "clearfix"}).find_all("li")
		player_informations = []




if __name__ == "__main__":
	engine = PlayersCrawler()

	links = engine.get_teams_links()
	
	players_links, team_title = engine.get_teams_info(links[0])

	engine.get_player_info(players_links[0], team_title)
