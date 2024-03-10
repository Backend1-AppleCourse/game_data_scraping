# game data scraping
# Topics:
# ● http
# ● web scraping
# ● data massaging
# ● matplotlib/numpy
# Task description:
# ● we will scrap the steam store for data regarding popular
# games.
# ● use this link (or any similar link showing games data).
# ● get the video game name and its genre descriptions. (i.e.
# strategy, action, etc).
# ● calculate and show in a plot the most appeared tags.
# ● give the user the option to select an input for a tag, and print
# the % of this tag from the games list.
# ● plot the user input tag with any relevant statistic.

import requests
import asyncio
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

class SteamGameScrapper:
    def __init__(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        url = 'https://store.steampowered.com'
        response = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def _get_top_sellers(self):
        topsellers_content = self.soup.find('div', {'id': 'tab_topsellers_content'})
        games = topsellers_content.find_all('a', class_=['tab_item'])
        return games


    def get_games(self):
        games = self._get_top_sellers()
        
        for index, game in enumerate(games):
            name = game.find('div', {'class': 'tab_item_name'})
            genre = game.find('span', {'class': 'top_tag'})
            print(index)
            if name:
                name = name.text
                print(name)
            if genre:
                genre = genre.text
                print(genre)

    def _get_tags(self, games):
        tags = {}
        for index, game in enumerate(games):
            genre = game.find('span', {'class': 'top_tag'})
            if genre:
                genre = genre.text
                if genre in tags:
                    tags[genre] += 1
                else:
                    tags[genre] = 1
        return tags

    # ● calculate and show in a plot the most appeared tags.
    def calculate_most_appeared_tags(self):
        games = self._get_top_sellers()

        tags = self._get_tags(games)
        tags = dict(sorted(tags.items(), key=lambda item: item[1], reverse=True))
        x = list(tags.keys())
        y = list(tags.values())

        plt.bar(x, y)
        plt.show(block=False)

    # ● give the user the option to select an input for a tag, and print
    # the % of this tag from the games list.
    def print_tag_percentage(self):
        while True:
            games = self._get_top_sellers()

            tags = self._get_tags(games)

            tag = input('Enter a tag: ')

            total = sum(tags.values())
            print(f"Total games: {total}")
            print(f"Percentage of {tag}: {tags[tag] / total * 100}%")
            
            user_input = input("Do you want to continue? (y/n): ")
            if user_input == "n":
                break

    # ● get from user input tag, then plot it with the other statistics
    def plot_user_input_tag(self):
        games = self._get_top_sellers()

        tags = self._get_tags(games)

        tags = dict(sorted(tags.items(), key=lambda item: item[1], reverse=True))
        x = list(tags.keys())
        y = list(tags.values())

        tag = input('Enter a tag: ')

        plt.bar(x, y)
        plt.bar(tag, tags[tag])
        plt.show()

    def scrap_all(self):
        self.get_games()
        self.calculate_most_appeared_tags()
        self.print_tag_percentage()
        self.plot_user_input_tag()
