class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class FootballTeam:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def list_players(self):
        print(f"Players of {self.name}:")
        for player in self.players:
            print(f"{player.name} - {player.position}")

# Creating a football team
team_name = "Dream Team"
coach_name = "Coach Smith"
team = FootballTeam(team_name, coach_name)

# Adding players to the team
team.add_player(Player("John Doe", "Forward"))
team.add_player(Player("Jane Smith", "Midfielder"))
team.add_player(Player("David Brown", "Defender"))

# Listing all players in the team
team.list_players()
