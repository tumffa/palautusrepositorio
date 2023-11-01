import unittest
from statistics_service import StatisticsService
from player_reader import PlayerReader

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReader("/nhl-statistics-1/src/tests/stats_for_testing.txt"))