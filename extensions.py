from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_login import LoginManager



db = SQLAlchemy(app)
migrate = Migrate(app , db)
login_manager = LoginManager(app)