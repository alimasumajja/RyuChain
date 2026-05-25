import bcrypt

from utils.user_storage import (load_users, save_users)


def hash_password(password):
    password_bytes = (password.encode())
    salt = (bcrypt.gensalt())
    hashed_password = (bcrypt.hashpw(password_bytes, salt))
    return (hashed_password.decode())


def verify_password(password, hashed_password):
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode()
    )

def register_user(username, password):
    users = load_users()
    for user in users:
        if (user["username"] == username):
            return False

    new_user = {
        "username": username,
        "password": hash_password(password),
        "role": "user"
    }

    users.append(new_user)
    save_users(users)

    return True


def login_user(username,password):

    users = load_users()

    for user in users:

        username_match = (

            user["username"]
            ==
            username
        )

        if username_match:

            password_valid = (
                verify_password(
                    password,
                    user[
                        "password"
                    ]
                )
            )

            if password_valid:

                return user

    return None