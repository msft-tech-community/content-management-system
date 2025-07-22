from flask import Blueprint, render_template, jsonify
import datetime

# Created blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Homepage route - serves the main CDN interface"""
    return render_template('index.html', 
                         title='CDN Management System',
                         current_time=datetime.datetime.now())

@main.route('/health_check')
def health_check():
    """Health check endpoint for monitoring and load balancers"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'service': 'cdn-management-system',
        'version': '1.0.0'
    }), 200