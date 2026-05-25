import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

PRIVATE_KEY_PATH = ("keys/private/private_key.pem")
PUBLIC_KEY_PATH = ("keys/public/public_key.pem")


def generate_keys():
    os.makedirs("keys/private", exist_ok=True)
    os.makedirs("keys/public",exist_ok=True)

    if (os.path.exists(PRIVATE_KEY_PATH) and os.path.exists(PUBLIC_KEY_PATH)):
        return

    private_key = (rsa.generate_private_key(public_exponent=65537,key_size=2048))
    public_key = (private_key.public_key())

    with open(PRIVATE_KEY_PATH,"wb") as file:
        file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=(
                    serialization
                    .PrivateFormat
                    .TraditionalOpenSSL
                ),
                encryption_algorithm=(
                    serialization
                    .NoEncryption()
                )
            )
        )

    with open(PUBLIC_KEY_PATH,"wb") as file:
        file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=(
                    serialization
                    .PublicFormat
                    .SubjectPublicKeyInfo
                )
            )
        )