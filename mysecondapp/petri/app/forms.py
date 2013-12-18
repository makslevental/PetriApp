__author__ = 'max'

from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, validators, PasswordField, SubmitField
from wtforms.validators import Required, Length
from models import User

class LoginForm(Form):
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please a valid email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False

class SignupForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name", [validators.Required("Please enter your last name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please a valid email address.")])
    phonenumber = TextField("Phone number", [validators.Required("Please enter a phone number.")])
    keycode = PasswordField("Key Code", [validators.Required("Please enter a key code"),
                                         validators.Length(min=4, max=4, message=("Key Code is incorrect length"))])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        user = None
        user = User.query.filter_by(phonenumber=self.phonenumber.data.lower()).first()
        if user:
            self.phonenumber.errors.append("That phone number is already taken")
            return False
        else:
            return True

class EditForm(Form):
    nickname = TextField('nickname', validators=[Required()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True


class PostForm(Form):
    post = TextField('post', validators=[Required()])


class AddNumberForm(Form):
    firstname = TextField("First name", [validators.Required("Please enter your first name.")])
    lastname = TextField("Last name", [validators.Required("Please enter your last name.")])
    phonenumber = TextField("Phone number", [validators.Required("Please enter a phone number.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

