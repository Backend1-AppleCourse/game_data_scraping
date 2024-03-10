from game_data_scraping import SteamGameScrapper
import asyncio

if __name__ == "__main__":
    steam_game_scrapper = SteamGameScrapper()
    steam_game_scrapper.scrap_all()

    