def mine_block(block):

    target = "3910"

    while not block.hash.startswith(
        target
    ):
        block.nonce += 1
        block.hash = (
            block.calculate_block_hash()
        )

    return block