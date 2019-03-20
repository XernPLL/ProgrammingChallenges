from app import db, login
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique=True)
    todos = db.relationship('Todo', backref = 'author', lazy = 'dynamic')
    progros = db.relationship('Inprogress', backref = 'author', lazy = 'dynamic')
    donos = db.relationship('Done', backref = 'author', lazy = 'dynamic')
    removos = db.relationship('Remove', backref = 'author', lazy = 'dynamic')

    def todoposts(self):
        return Todo.query.filter(self.id==Todo.user_id).order_by(Todo.timestamp.desc())

    def inprogressposts(self):
        return Inprogress.query.filter(self.id==Inprogress.user_id).order_by(Inprogress.timestamp.desc())

    def doneposts(self):
        return Done.query.filter(self.id==Done.user_id).order_by(Done.timestamp.desc())

    def removeposts(self):
        return Remove.query.filter(self.id==Remove.user_id).order_by(Remove.timestamp.desc())

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<Todo {}'.format(self.body)


class Inprogress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<In progress {}'.format(self.body)


class Done(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Done {}'.format(self.body)


class Remove(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Remove {}'.format(self.body)