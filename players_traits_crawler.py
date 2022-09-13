from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

class Players_Crawler:
    url: str = 'https://www.mykhel.com/football/fifa-world-cup-2022-squads-l4/'

    def __init__(self):
        options = Options()
        options.set_preference('intl.accept_languages', 'en-GB')

        self.browser = webdriver.Firefox(options=options)

    def clear_string(c : str):
            c = c.rstrip()
            c = c.lstrip()
            c = c.replace('-', ' ')
            c = c.replace(' ', '_')
            c = c.lower()
            return c

    def get_players_traits(self) -> list[str]:
        url = Players_Crawler.url

        self.browser.get(url)

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')

        teams_div = soup.find('div', { 'class': 'os-fifateams' })

        teams_blocks = teams_div.findChildren("div", recursive=False)

        links = [a['href'] for a in teams_blocks]
        return links
        # if genres:
        #     for g in genres:
        #         result.append(GB_Crawler.clear_string(g['data-entityname']))
        # else:
        #     result.append(GB_Crawler.clear_string(genres_div.get_text()))

        # return result


if __name__ == '__main__':
    engine = Players_Crawler()
    links = engine.get_players_traits()
    
    with open('tests.txt', 'w') as f:
        for link in links:
            f.write(f"{link}\n")

    # titles = [
    #     'Harry Potter and the Philosopher\'s Stone',
    #     'The Hunger Games',
    #     'The Hive',
    #     'Twilight',
    #     'The Fiery Cross',
    #     'The Hobbit and The Lord of the Rings'
    # ]

    # engine = GB_Crawler()
    # for t in titles:
    #     categories = engine.get_book_categories(t)
    #     print(categories)