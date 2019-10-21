import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or "aba3205bbb2e4be3a8123364505f16f5"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or "smtp.googlemail.com"
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "playersoft1999@gmail.com"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['playersoft1999@gmail.com']
    POSTS_PER_PAGE = 10
