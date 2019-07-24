# -*- coding:utf-8 -*-
from flask import Flask, render_template
from extensions import db, mail, debug_toolbar, migrate, api
from setting import DevConfig
from main.main import bp_main
import commands
from api.schedule import Schedule, ScheduleList
from api.odstable import OdsTable, OdsTableList
from api.datasource import Datasource, DatasourceList
from api.job import Job, JobList


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_api_resources(api)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    mail.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(bp_main)
    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


def register_shellcontext(app):
    def shell_context():
        return {
            'db': db
        }

    app.shell_context_processor(shell_context)


def register_commands(app):
    pass


def register_api_resources(api):
    api.add_resource(Schedule, '/schedules/<string:id>')
    api.add_resource(ScheduleList, '/schedules')
    api.add_resource(Job, '/jobs/<string:id>')
    api.add_resource(JobList, '/jobs')
    api.add_resource(Datasource, '/datasources/<string:id>')
    api.add_resource(DatasourceList, '/datasources')
    api.add_resource(OdsTable, '/odstables/<string:id>')
    api.add_resource(OdsTableList, '/odstables')
