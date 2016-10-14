import os
import importlib

import exceptions


def register_blueprints(app, application_package_name=None, blueprint_directory=None):
    """Register Flask blueprints on app object"""
    if not application_package_name:
        application_package_name = 'app'

    if not blueprint_directory:
        blueprint_directory = os.path.join(os.getcwd(), application_package_name)

    blueprint_directories = get_child_directories(blueprint_directory)

    for directory in blueprint_directories:
        abs_package = '{}.{}'.format(application_package_name, directory)

        service = importlib.import_module(abs_package)
        app.register_blueprint(service.blueprint_api, url_prefix='')


def get_child_directories(path):
    """Return names of immediate child directories"""
    if not _is_valid_directory(path):
        raise exceptions.InvalidDirectory

    entries = os.listdir(path)
    directory_names = []

    for entry in entries:
        abs_entry_path = os.path.join(path, entry)
        if _is_valid_directory(abs_entry_path):
            directory_names.append(entry)

    return directory_names


def _is_valid_path(path):
    """Return True if valid path"""
    return os.path.exists(path)


def _is_valid_directory(path):
    """Return True if valid directory"""
    return os.path.isdir(path)
