from lol_stats.riot_client import RiotClient

client = RiotClient()

account = client.get_account(
    game_name="KC NEXT ADKING",
    tag_line="EUW",
)

print(f"Riot ID : {account['gameName']} #{account['tagLine']}")

print(f"PUUID : {account['puuid']}")