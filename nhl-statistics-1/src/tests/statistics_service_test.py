import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_existing_name(self):
        #paluttaa playerluokkaisen olion:
        self.assertEqual(self.stats.search("Semenko"), Player("Semenko", "EDM", 4, 12))

    def test_search_nonexistent_name(self):
        #paluttaa None
        self.assertEqual(self.stats.search("Tomas"), None)
    
    def test_team_function(self):
        #method 'team' returns correct list of player objects in EDM team
        list_of_names = [player.name for player in self.stats.team("EDM")]
        self.assertEqual(list_of_names, ["Semenko", "Kurri", "Gretzky"])
    
    def test_top_2_players(self):
        #returns two players with top points
        top_2_names = [player.name for player in self.stats.top(1)]
        self.assertEqual(top_2_names, ["Gretzky", "Lemieux"])

    def test_top_2_by_assists(self):
        #returns top 2 players by assists
        top_2_names = [player.name for player in self.stats.top(1, 3)]
        self.assertEqual(top_2_names, ["Gretzky", "Yzerman"])

    def test_top_2_by_goals(self):
        #returns top 2 players by assists
        top_2_names = [player.name for player in self.stats.top(1, 2)]
        self.assertEqual(top_2_names, ["Lemieux", "Yzerman"])