from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct the core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('config.py')

    # Initialize database
    db.init_app(app)

    with app.app_context():
        from app.blueprints import index_route, add_task_route, modify_task_route
        app.register_blueprint(index_route.index_bp)
        app.register_blueprint(add_task_route.add_task_bp)
        app.register_blueprint(modify_task_route.modify_task_bp)

        db.create_all() # Create database tables

        return app
