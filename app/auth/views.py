from . import auth
from flask import render_template,redirect,url_for,request,flash
from .. import db
from .forms import RegistrationForm,LoginForm
from ..models import User
from flask_login import login_user,login_required,logout_user
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid email or Password')




    title = 'Login page'

    return render_template('login.html' ,title = title , login_form =form)


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        user = User(username = form.username.data ,email= form.email.data , password = form.password.data)
        db.session.add(user)
        db.session.commit()

        # mail_message("Welcome to the PITCH APP","welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))

    title = "New Account"

    return render_template('register.html',registration_form = form , title = title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


    