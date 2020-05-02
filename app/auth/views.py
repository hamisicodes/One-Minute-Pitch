from . import auth


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('auth/login.html')


@auth.route('/register',methods = ["GET","POST"])
def register():
    return render_template('auth/register.html')


@auth.route('/logout')
def logout():
    pass