import json
import os


USER_DB = (
    "database/users.json"
)


def ensure_user_db():

    os.makedirs(
        "database",
        exist_ok=True
    )

    if not os.path.exists(
        USER_DB
    ):

        with open(
            USER_DB,
            "w"
        ) as file:

            json.dump(
                [],
                file
            )


def load_users():

    ensure_user_db()

    with open(
        USER_DB,
        "r"
    ) as file:

        return json.load(
            file
        )


def save_users(
    users
):

    ensure_user_db()

    with open(
        USER_DB,
        "w"
    ) as file:

        json.dump(
            users,
            file,
            indent=4
        )