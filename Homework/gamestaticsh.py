class GameStats:


    def __init__(self, sideways_game):

        self.settings = sideways_game.settings
        self.reset_stats()

        # Start game in an active state.
        self.game_active = True

    def reset_stats(self):

        self.ships_left = self.settings.ship_limit