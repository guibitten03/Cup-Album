from bs4 import BeautifulSoup
import requests

class PlayersCrawler:
	url: str = "https://www.mykhel.com/football/fifa-world-cup-2022-squads-l4/"

	def __init__(self): return

	def get_players_traits(self) -> list[str]:
		page = requests.get(PlayersCrawler.url)

		soup = BeautifulSoup(page.content, "html.parser")

		teams_div = soup.find("div", { "class": "os-fifateams" })

		teams_blocks = teams_div.findChildren("div", recursive=False)

		return None


if __name__ == "__main__":
	engine = PlayersCrawler()
	links = engine.get_players_traits()
	print(links)