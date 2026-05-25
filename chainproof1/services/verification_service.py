from crypto.signature import (verify_signature)


def verify_document_in_chain(blockchain,document_hash):

    for block in (blockchain.chain):
        if (block.document_hash == document_hash):
            signature_valid = (verify_signature(document_hash,block.owner_signature))
            return {
                "found": True,
                "block_index": block.index,

                "timestamp": block.timestamp,

                "block_hash": block.hash,

                "signature_valid": signature_valid
            }

    return {
        "found": False
    }