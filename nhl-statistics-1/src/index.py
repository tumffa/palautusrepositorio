from statistics_service import StatisticsService
from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def main():
    stats = StatisticsService(PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"))
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10, SortBy.GOALS)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

if __name__ == "__main__":
    main()
