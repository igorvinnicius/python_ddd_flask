from flask import render_template
from .. import main
from flask.ext.login import login_required, current_user


@main.route('/')
@login_required
def index():
	return render_template('main/index.html')
