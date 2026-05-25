from flask import Flask
from routes.blockchain_routes import (blockchain_bp)
from routes.verification_routes import (verification_bp)
from routes.auth_routes import (auth_bp)

app = Flask(__name__)

# Secret key untuk session login
app.secret_key = ("chainproof-secret")

# Folder upload
app.config["UPLOAD_FOLDER"] = "uploads"

# Register blueprint
app.register_blueprint(blockchain_bp)

app.register_blueprint(verification_bp)

app.register_blueprint(auth_bp)


if __name__ == "__main__":

    app.run(
    host="0.0.0.0",
    port=5000,
    debug=True
)