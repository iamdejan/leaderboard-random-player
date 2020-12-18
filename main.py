import json
import random
import sys

import names
from requests import post, Response


class Player:
    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name

    def __str__(self):
        return json.dumps(self.__dict__)


def store_player_data():
    name: str = names.get_full_name()
    score: int = random.randint(0, 200)
    player: Player = Player(score, name)
    response: Response = post(
        url="http://localhost:8888/players",
        json=player.__dict__,
        headers={"Content-Type": "application/json"}
    )
    print(f"player: {player}, status code: {response.status_code}")


def main():
    argv = sys.argv[1:]
    size: int = int(argv[0])
    for _ in range(size):
        store_player_data()


if __name__ == "__main__":
    main()
