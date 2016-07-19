from flask import render_template, redirect, request, url_for
from .. import shared
import os


from app.domain.services.authentication_service import AuthenticationService
from app.infrastructure.email.email_service import send_email

from ..forms.register_form import RegisterForm

@shared.route('/shared/register', methods=['GET'])
def register():
    return render_template('shared/register/register.html', form = RegisterForm())

@shared.route('/shared/register', methods=['POST'])
def execute_register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = form.get_user()
        AuthenticationService.register(user)

        token = AuthenticationService.generate_confirmation_account_token(user.id)
        send_email(user.email, 'Confirm Your Account',
                    'mail/confirm', user=user, token=token)

        print os.getenv('MAIL_USERNAME')

        return redirect(url_for('shared.login'))
    return render_template('shared/register/register.html',  form = form)
