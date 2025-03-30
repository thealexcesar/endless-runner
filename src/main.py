import os.path

from game import Game

assets = "../assets"
if __name__ == "__main__":
    os.makedirs(assets) if not os.path.exists(assets) else print("Assets folder already exists.")
    game = Game()
    game.run()