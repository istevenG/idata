# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_restful import Api

db = SQLAlchemy()
mail = Mail()
debug_toolbar = DebugToolbarExtension()
migrate = Migrate()
api = Api(prefix='/api/v1')
