from app import db, app
from hashlib import md5
from werkzeug import generate_password_hash, check_password_hash


ROLE_USER = 0
ROLE_ADMIN = 1

# followers = db.Table('followers',
#                      db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
#                      db.Column('followed_id', db.Integer, db.ForeignKey('user.id')))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(120), unique=True)
    phonenumber = db.Column(db.String(10), unique=True)
    pwdhash = db.Column(db.String(54))
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    # backref here defines a way to access the 'owner' from the tele, ie phonenumbers.owner will
    # return the user
    phonenumbers = db.relationship('Phonenumbers', backref='owner', lazy='dynamic')

    def __init__(self, firstname, lastname, email, phonenumber, password):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.email = email.lower()
        self.phonenumber = phonenumber.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() == None:
                break
            version += 1
        return new_nickname

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email).hexdigest() + '?d=mm&s=' + str(size)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r %r %r %r>' % (self.firstname, self.lastname, self.email, self.phonenumber)


class Phonenumbers(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    number = db.Column(db.String(10), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<phonenumber %r firstname %r lastname %r>' % (self.number, self.firstname, self.lastname)

