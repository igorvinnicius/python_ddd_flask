from flask import render_template
from .. import blog
from flask.ext.login import login_required, current_user

@blog.route('/blog')
@login_required
def index():
	return render_template('blog/index.html')
