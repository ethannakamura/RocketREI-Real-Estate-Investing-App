from flask import Flask
from config import Config

from .api.routes import api
from .auth.routes import auth

app = Flask(__name__)

app.config.from_object(Config)

# urlprefix defines inside() of route when accessing in url
# so we dont need to define in route
app.register_blueprint(api)
app.register_blueprint(auth)

from . import routes