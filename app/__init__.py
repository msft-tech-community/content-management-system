from flask import Flask
from config import config

def create_app(config_name='development'):
    """Application factory pattern for Flask app creation"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Register blueprints
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app