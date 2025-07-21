import os
from app import create_app

# Create Flask app instance
app = create_app(os.getenv('FLASK_ENV') or 'development')

if __name__ == '__main__':
    # Development server settings
    app.run(
        host='0.0.0.0',  # Makes it accessible from other devices
        port=5000,
        debug=app.config['DEBUG']
    )