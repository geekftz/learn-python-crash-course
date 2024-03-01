class GameStats():
    """tracking game statistics"""
    def __init__(self, ai_settings):
        # initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()

        # the game is not active at the beginning
        self.game_active = False

    def reset_stats(self):
        """initialize statistics that may change during game runtime"""
        self.ships_left = self.ai_settings.ship_limit
