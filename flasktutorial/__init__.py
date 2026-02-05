import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flasktutorial.config import Config


# Create a new Flask web application
# 'app' is the variable that stores our Flask app object
# '__name__' tells Flask that this file is the main program
# Flask uses this to know where to look for templates and static files


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


# print("MAIL USER:", app.config["MAIL_USERNAME"])
# print("MAIL PASS LENGTH:", len(app.config["MAIL_PASSWORD"]) if app.config["MAIL_PASSWORD"] else None)



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flasktutorial.users.routes import users
    from flasktutorial.posts.routes import posts
    from flasktutorial.main.routes import main
    from flasktutorial.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
    
