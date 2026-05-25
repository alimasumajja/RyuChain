from blockchain.hash_utils import (calculate_hash)


class Block:

    def __init__(
        self,
        index,
        timestamp,
        document_hash,
        previous_hash,
        owner_signature="",
        nonce=0
    ):

        self.index = index
        self.timestamp = timestamp
        self.document_hash = document_hash
        self.previous_hash = previous_hash
        self.owner_signature = owner_signature
        self.nonce = nonce

        # hash awal block
        self.hash = (self.calculate_block_hash())

    def calculate_block_hash(self):

        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "document_hash":
                self.document_hash,
            "previous_hash":
                self.previous_hash,
            "owner_signature":
                self.owner_signature,
            "nonce":
                self.nonce
        }

        return calculate_hash(block_data)

    def to_dict(self):

        return {
            "index":
                self.index,
            "timestamp":
                self.timestamp,
            "document_hash":
                self.document_hash,
            "previous_hash":
                self.previous_hash,
            "owner_signature":
                self.owner_signature,
            "nonce":
                self.nonce,
            "hash":
                self.hash
        }

    @classmethod
    def from_dict(
        cls,
        data
    ):

        block = cls(
            index=data["index"],
            timestamp=
                data["timestamp"],
            document_hash=
                data[
                    "document_hash"
                ],
            previous_hash=
                data[
                    "previous_hash"
                ],
            owner_signature=
                data.get(
                    "owner_signature",
                    ""
                ),
            nonce=data["nonce"]
        )

        # pakai hash lama dari JSON
        block.hash = (
            data["hash"]
        )

        return block