class GameStats:
    """Track stastics for Alien Invasion."""
    def __init__(self,aigame):
        """Initialize statistics."""
        self.settings=aigame.settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active=False
        # Start Fleet Of Aliens in an active state.
        self.game_active=True
        # High score should never be reset.
        self.high_score=0
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left=self.settings.ship_limit
        self.score=0
        self.level=1