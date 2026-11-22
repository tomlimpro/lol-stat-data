import httpx

from lol_stats.config import RIOT_API_KEY

"""
riot_client.py : Porte d'entrée vers Riot


"""

class RiotClient:
    BASE_URL = "https://europe.api.riotgames.com"

    def __init__(self) -> None:
        self.headers = {
            "X-Riot-Token":RIOT_API_KEY,
        }
    
    def get_account(self, game_name: str, tag_line: str) -> dict:
        url = (
            f"{self.BASE_URL}/riot/account/v1/accounts/"
            f"by-riot-id/{game_name}/{tag_line}"
        )

        response = httpx.get(
            url,
            headers=self.headers,
            timeout=10.0,
        )

        response.raise_for_status()
        
        return response.json()