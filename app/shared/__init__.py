from flask import Blueprint

shared = Blueprint('shared',__name__)

from .controllers import authentication_controller, register_controller
