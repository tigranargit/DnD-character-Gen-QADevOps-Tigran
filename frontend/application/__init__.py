from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import getenv
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ("mysql+pymysql://" + getenv('MYSQL_USER') + ":" + getenv('MYSQL_PWD') + "@" + getenv('MYSQL_IP') + "/" + getenv('MYSQL_DB'))
app.config['SECRET_KEY'] = getenv('MYSQL_SK')

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

xray_recorder.configure(service='My application')
XRayMiddleware(app, xray_recorder)

from application.models import user, feat

db.create_all()
db.session.commit()

aFeat = feat("Test Feat", "This is a filler data", "non")
db.session.add(aFeat)
db.session.commit()

from application import routes