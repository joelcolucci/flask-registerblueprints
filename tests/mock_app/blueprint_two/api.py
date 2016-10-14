import os

from flask import Blueprint
from flask import render_template


SERVICE_NAME = 'blueprint_two'

# Blueprint pattern requires absolute path to template folder
CURRENT_DIRECTORY = os.path.dirname(__file__)
TEMPLATE_FOLDER = os.path.join(CURRENT_DIRECTORY, 'templates')


blueprint_api = Blueprint(SERVICE_NAME,
                          __name__,
                          static_url_path='',
                          static_folder='static',
                          template_folder=TEMPLATE_FOLDER)


@blueprint_api.route('/blueprint-two', methods=['GET'])
def get_root():
    """Return home template"""
    return render_template('{}/index.html'.format(SERVICE_NAME))
