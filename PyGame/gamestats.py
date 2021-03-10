class GameStats:
    # Track statistics for alien invasion

    def __init__(self, ai_game):
        # initialize statisitcs
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset (not in reset_stats)
        self.high_score = 0

    def reset_stats(self):
        # initialize stats that can change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1