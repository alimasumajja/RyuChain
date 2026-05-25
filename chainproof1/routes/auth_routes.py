from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session
)

from services.auth_service import (register_user,login_user)


auth_bp = Blueprint("auth",__name__)


# ======================
# REGISTER
# ======================
@auth_bp.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    message = ""

    if request.method == "POST":

        username = (
            request.form[
                "username"
            ]
        )

        password = (
            request.form[
                "password"
            ]
        )

        success = (
            register_user(
                username,
                password
            )
        )

        if success:

            return redirect(
                "/login"
            )

        message = (
            "Username sudah digunakan"
        )

    return render_template(
        "register.html",
        message=message
    )


# ======================
# LOGIN
# ======================
@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    message = ""

    if request.method == "POST":

        username = (
            request.form[
                "username"
            ]
        )

        password = (
            request.form[
                "password"
            ]
        )

        user = (
            login_user(
                username,
                password
            )
        )

        if user:

            session[
                "user"
            ] = user[
                "username"
            ]

            session[
                "role"
            ] = user[
                "role"
            ]

            return redirect(
                "/"
            )

        message = (
            "Username atau password salah"
        )

    return render_template(
        "login.html",
        message=message
    )


# ======================
# LOGOUT
# ======================
@auth_bp.route(
    "/logout"
)
def logout():

    session.clear()

    return redirect(
        "/login"
    )