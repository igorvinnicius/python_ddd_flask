from flask import abort
from flask.ext.login import current_user
from functools import wraps

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):

            if role == 'ADMIN' and not current_user.is_admin:
                abort(403)

            if role == 'BLOGER' and not current_user.is_bloger:
                abort(403)

            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    return role_required("ADMIN")(f)

def bloger_required(f):
    return role_required("BLOGER")(f)
