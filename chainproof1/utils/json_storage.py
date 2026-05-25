import json
import os


DB_PATH = ("database/blockchain.json")


def ensure_database_exists():

    folder = os.path.dirname(
        DB_PATH
    )

    os.makedirs(
        folder,
        exist_ok=True
    )

    if not os.path.exists(
        DB_PATH
    ):

        with open(
            DB_PATH,
            "w"
        ) as file:

            json.dump([], file)


def save_chain(chain):
    ensure_database_exists()
    data = [
        block.to_dict()
        for block in chain
    ]
    with open(
        DB_PATH,
        "w"
    ) as file:
        json.dump(
            data,
            file,
            indent=4
        )


def load_chain():

    ensure_database_exists()

    with open(DB_PATH,"r") as file:
        return json.load(file)