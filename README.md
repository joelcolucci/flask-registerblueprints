# Flask Register Blueprints
Dynamically register blueprints. No more hard coding imports.

## Installation
```
pip install Flask-RegisterBlueprints
```

## Getting Started
An example application can be found under the tests directory as "mock_app".

### Required blueprint naming conventions
Blueprints must be created with the name `blueprint_api`.

```python
blueprint_api = Blueprint(NAME)

@blueprint_api.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')
```

### App initialization and blueprint registration
```python
import os

from flask import Flask
from flask_registerblueprints import register_blueprints


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py', silent=True)


app_pkg_name = 'mock_app'
abs_bp_dir = os.path.join(os.getcwd(),'mock_app')

register_blueprints(app,
                    application_package_name='mock_app',
                    blueprint_directory=abs_bp_dir)
```

## License
MIT License Copyright (c) 2016 Joel Colucci