from flask_sqlalchemy import SQLAlchemy #ORM(translates between SQL & python)

from flask_login import LoginManager, UserMixin #says user obj should inherit 
# from db.Model and UserMixin to work as users of our site eligible for Login 
# Management
from datetime import datetime, timezone

from werkzeug.security import generate_password_hash
from uuid import uuid4

# my instance of SQLAlchemy
db = SQLAlchemy()

# my var instance of login manager 
login = LoginManager()

# asking login manager to work with a db of our creation so we need
# to set up translation between our login manager and our db
# gives login mangr access to the whole user object
# NECESSARY to use with login manager
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# my user object
class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=True, default='')
    last_name = db.Column(db.String(100), nullable=True, default='')
    password = db.Column(db.String(150), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __init__(self, username, email, password, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name= first_name
        self.last_name= last_name
        self.password= generate_password_hash(password)
        self.id = str(uuid4())

        # we need to log users and keep track of who is logged in/who reqd to log in
        # the login manager maintains user session management during periods of use