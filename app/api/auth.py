from flask import g
from flask_httpauth import HTTPBasicAuth
from app.models import User
from app.api.errors import error_response

basic_auth = HTTPBasicAuth()

@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return error_response(401)
