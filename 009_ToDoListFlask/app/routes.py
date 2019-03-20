from flask import render_template, flash, redirect, url_for, jsonify, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, NewForm
from app.models import User, Todo, Inprogress, Done


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for("todolist"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('todolist'))
    return render_template('login.html',  title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/todolist', methods=['GET', 'POST'])
@login_required
def todolist():
    form = NewForm()
    if form.validate_on_submit():
        todo = Todo(body=form.newtodo.data, author=current_user)
        print(todo)
        db.session.add(todo)
        db.session.commit()
        flash('Added')
        return redirect(url_for('todolist'))
    todoposts = current_user.todoposts().all()
    inprogressposts = current_user.inprogressposts().all()
    doneposts = current_user.doneposts().all()
    return render_template("todolist.html", title='To-Do List', form=form, todoposts=todoposts,
                           inprogressposts=inprogressposts, doneposts= doneposts)

@app.route('/_removeobject')
def removeobject():
    type = request.args['type']
    a = request.args['a']
    me = eval(type+".query.filter_by(body=a, author=current_user).first()")
    db.session.delete(me)
    db.session.commit()

    return jsonify(result=a)

@app.route('/_addobject')
def addobject():
    type = request.args['type']
    a = request.args['a']
    me = eval(type+"(body=a, author=current_user)")
    db.session.add(me)
    db.session.commit()

    return jsonify(result=a)
