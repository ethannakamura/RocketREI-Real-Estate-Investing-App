#__init__.py estabs comms between our apps and svcs
from flask import Flask
from config import Config

# my blueprints
from .api.routes import api
from .auth.routes import auth

# my db info (instance of db obj)
# import db login mngr from my models file
from .models import db, login
from flask_migrate import Migrate

from .calculators.routes import calculators

#function is for dash and flask communication
# create instance of my flask obj (creation of flask app)
# create core Flask app with embedded Dash app
app = Flask(__name__)
app.config.from_object(Config)
# configs my flask app based on config class
# conigs my dash app onto my parent flask app

# register my bp's - creates comms
app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(calculators)

# creates my ORM and Migrate comms
db.init_app(app)
migrate = Migrate(app, db)

# configs my login mngr
login.init_app(app)
# stops unlogged user from accessing a page and redirects
login.login_view = 'auth.signin'
login.login_message = '_LOGIN_REQUIRED_TO_ACCESS_INVESTING_TOOLS'
login.login_message_category = 'danger'

# allows my whole app's access to comm w/routes
from . import routes

# let app/flask obj access my db models
from . import models