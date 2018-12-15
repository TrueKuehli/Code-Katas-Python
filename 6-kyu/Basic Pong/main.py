class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.round = 0
        self.scores = [0, 0]
        self.game_over = False

    def play(self, ball_pos, player_pos):
      if self.game_over:
        return "Game Over!"
      else:
        player = (self.round & 1) + 1
        opponent = ((self.round & 1) ^ 1) + 1
        self.round += 1

        if (player_pos - 3) <= ball_pos <= (player_pos + 3):
          return "Player " + str(player) + " has hit the ball!"
        else:
          self.scores[opponent - 1] += 1
          if self.scores[opponent - 1] >= self.max_score:
            self.game_over = True
            return "Player " + str(opponent) + " has won the game!"
          else:
            return "Player " + str(player) + " has missed the ball!"

game = Pong(2)
print(game.play(50, 53), "Player 1 has hit the ball!")
print(game.play(100, 97), "Player 2 has hit the ball!")
print(game.play(0, 4), "Player 1 has missed the ball!")
print(game.play(25, 25), "Player 2 has hit the ball!")
print(game.play(75, 25), "Player 2 has won the game!")
print(game.play(50, 50), "Game Over!")
