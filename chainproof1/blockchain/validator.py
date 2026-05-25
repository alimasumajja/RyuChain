def validate_chain(chain):

    for i in range(1, len(chain)):

        current = chain[i]
        previous = chain[i - 1]

        # Hitung ulang hash block
        recalculated_hash = (
            current.calculate_block_hash()
        )

        # Cek isi block berubah
        if current.hash != recalculated_hash:

            return (
                False,
                f"Block {i} hash invalid"
            )

        # Cek relasi chain rusak
        if (
            current.previous_hash
            != previous.hash
        ):

            return (
                False,
                f"Block {i} previous hash mismatch"
            )

    return (
        True,
        "Blockchain valid"
    )