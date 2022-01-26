from flask import Flask
from config import Config
from flask_migrate import Migrate
from . models import login
from . models import db 
from .dash_application import fair_market_rent, fair_market_rent2, fair_market_rent3, fair_market_rent4

migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app,db)
    login.login_view = 'auth.signin'
    login.login_message = '_LOGIN_REQUIRED_TO_ACCESS_INVESTING_TOOLS'
    login.login_message_category = 'danger'
    
    from .auth.routes import auth
    from .calculators.routes import calculators

    app.register_blueprint(auth)
    app.register_blueprint(calculators)

    fair_market_rent(app)
    fair_market_rent2(app)
    fair_market_rent3(app)
    fair_market_rent4(app)

    with app.app_context():
        from . import routes

    from . import models

    return app