import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from werkzeug.utils import (secure_filename)
from blockchain.blockchain import (Blockchain)
from crypto.hashing import (hash_document)
from crypto.key_manager import (generate_keys)
from crypto.signature import (sign_document)

blockchain_bp = Blueprint(
    "blockchain",
    __name__
)

generate_keys()

blockchain = Blockchain()


@blockchain_bp.route("/")
def home():

    return render_template(
        "index.html"
    )


@blockchain_bp.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload_document():
    if "user" not in session:

        return redirect(
        "/login"
    )

    message = ""

    if request.method == "POST":

        uploaded_file = (
            request.files["file"]
        )

        if uploaded_file:

            filename = (
                secure_filename(
                    uploaded_file.filename
                )
            )

            file_path = os.path.join(
                "uploads",
                filename
            )

            uploaded_file.save(
                file_path
            )

            document_hash = (
                hash_document(
                    file_path
                )
            )

            signature = (
                sign_document(
                    document_hash
                )
            )

            blockchain.add_block(
                document_hash,
                signature
            )

            message = (
                "Dokumen berhasil "
                "didaftarkan"
            )

    return render_template(
        "upload.html",
        message=message
    )


@blockchain_bp.route(
    "/blockchain"
)

def show_blockchain():

    blockchain = (Blockchain())

    is_valid, message = (blockchain.is_chain_valid())

    return render_template(
        "blockchain.html",

        chain= blockchain.chain,

        blockchain_valid= is_valid,

        validation_message= message
    )