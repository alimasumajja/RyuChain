from datetime import datetime
from blockchain.block import Block
from blockchain.pow import mine_block
from utils.json_storage import (save_chain,load_chain)


class Blockchain:

    def __init__(self):
        self.chain = []
        self.load_or_create_chain()

    def load_or_create_chain(self):

        loaded_chain = (load_chain())
        if loaded_chain:

            self.chain = [

                Block.from_dict(block)

                for block in loaded_chain
            ]

            print("Blockchain loaded.")

        else:

            self.create_genesis_block()

            save_chain(self.chain)

            print("Genesis block created.")

    def create_genesis_block(self):

        genesis_block = Block(
            index=0,
            timestamp=str(datetime.now()),
            document_hash="GENESIS",
            previous_hash="0"
        )

        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(
        self,
        document_hash,
        owner_signature
    ):

        # Cek duplicate
        for block in self.chain:

            if (block.document_hash == document_hash):
                print("Dokumen sudah terdaftar!")
                return

        previous_block = (self.get_latest_block())

        new_block = Block(
            index=len(self.chain),
            timestamp = str(datetime.now()),
            document_hash = document_hash,
            previous_hash=(previous_block.hash),
            owner_signature = owner_signature
        )

        mined_block = (mine_block(new_block))
        self.chain.append(mined_block)
        save_chain(self.chain)
    
    def is_chain_valid(self):

        for i in range(
            1,
            len(self.chain)
        ):

            current_block = (
                self.chain[i]
            )

            previous_block = (
                self.chain[i - 1]
            )

            recalculated_hash = (
                current_block
                .calculate_block_hash()
            )

            # cek hash block
            if (
                current_block.hash
                !=
                recalculated_hash
            ):

                return (
                    False,
                    f"Block "
                    f"{current_block.index} "
                    f"hash invalid"
                )

            # cek previous hash
            if (
                current_block
                .previous_hash
                !=
                previous_block.hash
            ):

                return (
                    False,
                    f"Block "
                    f"{current_block.index} "
                    f"previous hash mismatch"
                )

            # cek PoW
            if not (
                current_block.hash
                .startswith(
                    "3910"
                )
            ):

                return (
                    False,
                    f"Block "
                    f"{current_block.index} "
                    f"invalid PoW"
                )

        return (
            True,
            "Blockchain valid"
        )