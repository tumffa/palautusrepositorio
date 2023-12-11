from statistics_1 import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    matcher = And(
    HasFewerThan(2, "goals"),
    PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)

    matcher = And(
    Not(HasAtLeast(2, "goals")),
    PlaysIn("NYR")
    )
    
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
