from crypt import methods
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jesse'}
    posts = [
        {
            'author': {'username': 'Frank Piazzo'},
            'body': """Man arrested After stealing 20,0000 Hamsters
             and trying to cross into Canada!"""
        },
        {
            'author': {'username': 'John'},
            'body': """fucking Flop I hate fucking
             tony stark, but Black Widow was hot as fuck id put in her ass"""
        }


    ]

    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)