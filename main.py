from game import *

player1 = Player(1, "Alice")
player2 = Player(2, "Bob")
player3 = Player(3, "Charlie")
player4 = Player(4, "David")
player5 = Player(5, "Eve")
player6 = Player(6, "Frank")
player7 = Player(7, "Grace")
player8 = Player(8, "Hank")
player9 = Player(9, "Ivy")
player10 = Player(10, "John")

game = GameManager()

game.add_player(player1)
game.add_player(player2)
game.add_player(player3)
game.add_player(player4)
game.add_player(player5)
game.add_player(player6)
game.add_player(player7)
game.add_player(player8)
game.add_player(player9)
game.add_player(player10)

game.assign_roles()