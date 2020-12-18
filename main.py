import random
import sys
from typing import List

import names


class Player:
    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name


def main():
    argv = sys.argv[1:]
    size: int = int(argv[0])

    players: List[Player] = []
    for _ in range(size):
        name: str = names.get_full_name()
        score: int = random.randint(0, 200)
        players.append(Player(score, name))
    pass


if __name__ == "__main__":
    main()
