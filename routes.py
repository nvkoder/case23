from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
import time


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Tillykke, du er en registreret bruger!')
        return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    logout_user()
    if current_user.is_authenticated:
        return redirect(url_for('welcome'))  # Redirect authenticated users to welcome page

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('welcome'))  # Redirect to welcome page after successful login
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')  # Provide feedback for failed login
    
    return render_template('login.html', title='Login', form=form)






@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title='Welcome')


@app.route('/preferencer')
def preferencer():
    return render_template('preferencer.html')


