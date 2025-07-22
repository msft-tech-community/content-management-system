from flask import Flask
from config import config
import os
services_path = os.path.join(os.path.dirname(__file__), 'services')
if not os.path.exists(services_path):
    os.makedirs(services_path)


def create_app(config_name='development'):
    """Application factory pattern for Flask app creation"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Register blueprints
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app