from . import auth
from flask import render_template,redirect,url_for
from .. import db
from .forms import RegistrationForm
from ..models import User


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(username = form.username.data ,email= form.email.data , password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"

    return render_template('register.html',registration_form = form)


@auth.route('/logout')
def logout():
    pass