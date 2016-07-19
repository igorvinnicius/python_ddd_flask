from flask import Blueprint

admin = Blueprint('admin',__name__)

from .controllers import admin_controller