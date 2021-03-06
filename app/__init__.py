from flask import Flask
from config import config_options
from flask_bootsrap import Bootsrap

#initializing bootsrap extension
bootstrap = Bootsrap()

def create_app(config_name):

    #initializing application
    app = Flask(__name__,instance_relative_config = True)

    #creating configurations
    app.config.from_object(config_options[config_name])

    #initialize flask extensions
    bootstrap.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #set up configurations
    from requests import configure_request
    configure_request(app)

    return app

