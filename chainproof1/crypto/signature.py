import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import (padding)
from cryptography.hazmat.primitives import (serialization)
from cryptography.exceptions import (InvalidSignature)


PRIVATE_KEY_PATH = ("keys/private/private_key.pem")

PUBLIC_KEY_PATH = ("keys/public/public_key.pem")


def sign_document(document_hash):

    with open( PRIVATE_KEY_PATH, "rb") as file:
        private_key = (serialization.load_pem_private_key(file.read(), password=None))

    signature = (
        private_key.sign(document_hash.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=(padding.PSS.MAX_LENGTH)
            ),
            hashes.SHA256()
        )
    )

    return (base64.b64encode(signature).decode())


def verify_signature(document_hash, signature):

    with open(PUBLIC_KEY_PATH, "rb") as file:
        public_key = (serialization.load_pem_public_key(file.read()))

    try:
        public_key.verify(
            base64.b64decode(signature),
            document_hash.encode(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=(padding.PSS.MAX_LENGTH)
            ),

            hashes.SHA256()
        )
        return True

    except InvalidSignature:
        return False