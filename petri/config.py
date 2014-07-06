__author__ = 'max'
#i hate you
import os
basedir = '/var/www/mysecondapp/petri'
# basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/app.db'
SQLALCHEMY_MIGRATE_REPO = basedir + '/db_repository'

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'petriapp@gmail.com'
MAIL_PASSWORD = ''

ADMINS = ['maksim.levental@gmail.com']

# pagination
NUMBERS_PER_PAGE = 3
