from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
from . import routes

def create_app():
    from .routes import views
    from .auth import auth

    # urlprefix defines inside() of route when accessing in url
    # so we dont need to define in route
    app.register_blueprint(routes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app

