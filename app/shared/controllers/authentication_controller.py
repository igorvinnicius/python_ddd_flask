from flask import render_template, redirect, request, url_for
from .. import shared

import flask.ext.login
from flask.ext.login import login_user, logout_user, \
    current_user

from app.domain.services.authentication_service import AuthenticationService

from ..forms.login_form import LoginForm


@shared.route('/shared/login', methods=['GET'])
def login():
    return render_template('shared/authentication/login.html', form = LoginForm())

@shared.route('/shared/login', methods=['POST'])
def execute_login():

    form = LoginForm()

    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        AuthenticationService.login(user_email, user_password)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('shared/authentication/login.html',  form = form)

@shared.route('/shared/logout', methods=['GET'])
def execute_logout():
    AuthenticationService.logout_current_user()
    return redirect(url_for('main.index'))

@shared.route('/shared/confirmaccount/<token>')
def confirmaccount(token):

    AuthenticationService.confirm_user_account(token)
    return redirect(url_for('main.index'))
