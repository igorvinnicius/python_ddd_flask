from flask import Blueprint

blog = Blueprint('blog',__name__)

from .controllers import blog_controller