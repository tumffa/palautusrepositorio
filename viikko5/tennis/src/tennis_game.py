class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score1 = self.player1_score
        score2 = self.player2_score
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]

        if score1 == score2:
            if score1 < 3:
                return score_names[score1] + "-All"
            else:
                return "Deuce"
            
        elif score1 < 4 and score2 < 4:
            return score_names[score1] + "-" + score_names[score2]
        
        elif score1 > 3 or score2 > 3:
            if score1 - score2 == 1:
                return "Advantage player1"
            elif score2 - score1 == 1:
                return "Advantage player2"
            elif score1 - score2 >= 2:
                return "Win for player1"
            else:
                return "Win for player2"