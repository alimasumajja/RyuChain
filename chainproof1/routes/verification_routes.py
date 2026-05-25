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
from services.verification_service import (verify_document_in_chain)


verification_bp = Blueprint(
    "verification",
    __name__
)

# blockchain = Blockchain()


@verification_bp.route(
    "/verify",
    methods=["GET", "POST"]
)
def verify_document():

    result = None

    # reload blockchain terbaru
    blockchain = Blockchain()

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

            result = (
                verify_document_in_chain(
                    blockchain,
                    document_hash
                )
            )

    return render_template(
        "verify.html",
        result=result
    )