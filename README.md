# Microblog-Flask

Blog on Flask
Created using https://habr.com/ru/post/346306/

## How to start
Clone repository
Create and activate a virtual environment

```commandline
$ virtual venv --python=python3.7
$ source venv/bin/activate
```
Install the required modules
```commandline
$ pip install -r requirements.txt
```
Create a database
```commandline
$ python manage.py db init
$ python manage.py db migrate -m "init"
$ python manage.py db upgrade
```
Set environment variables
```commandline
$ export FLASK_APP=the_microblog.py
$ export SECRET_KEY=<secret-key>
$ export MS_TRANSLATOR_KEY=<your-key>
$ export MAIL_SERVER=smtp.googlemail.com
$ export MAIL_PORT=587
$ export MAIL_USE_TLS=1
$ export MAIL_USERNAME=<your-gmail-username>
$ export MAIL_PASSWORD=<your-gmail-password>
```
Run flask on localhost
```commandline
$ flask run
```
