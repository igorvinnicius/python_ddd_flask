from flask import Blueprint

main = Blueprint('main', __name__)

from .controllers import main_controller