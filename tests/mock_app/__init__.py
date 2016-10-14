from flask import Flask
from flask_registerblueprints import register_blueprints

import os


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)


app_pkg_name = 'mock_app'
abs_bp_dir = os.path.join(os.getcwd(),'tests/mock_app')

register_blueprints(app,
                    application_package_name='mock_app',
                    blueprint_directory=abs_bp_dir)
