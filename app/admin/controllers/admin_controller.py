from flask import render_template
from .. import admin
from flask.ext.login import login_required, current_user

@admin.route('/admin')
@login_required
def index():
	return render_template('admin/index.html')
