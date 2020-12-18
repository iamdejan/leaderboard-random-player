import json
import multiprocessing
import random
import sys

import names
from requests import post


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
    post(
        url="http://localhost:8888/players",
        json=player.__dict__,
        headers={"Content-Type": "application/json"}
    )


THREADS: int = 4


def main():
    argv = sys.argv[1:]
    size: int = int(argv[0])
    remainder: int = size // THREADS

    chunk = [0 for _ in range(THREADS)]
    chunks = [chunk for _ in range(remainder)]

    processes = []
    for _ in chunks:
        p = multiprocessing.Process(target=store_player_data)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
