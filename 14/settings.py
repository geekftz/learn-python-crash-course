class Settings():
    # A class that stores all settings for Alien Invasion
    def __init__(self):
        # initialize game setting
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 3
        # if fleet_direction is 1 means move to the right, and -1 means move to the left
        self.fleet_direction = 1

        # At what speed to accelerate the game pace
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change as the game progresses"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction is 1, indicating to the right; -1 means left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale



