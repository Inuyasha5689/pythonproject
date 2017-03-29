from flask import Flask
from flask_cors import CORS, cross_origin

def create_app(config_filename):
    app = Flask(__name__, static_folder='templates/static')
    CORS(app)
    app.config.from_object(config_filename)

    from app.models import db
    db.init_app(app)

    from app.controller import users
    app.register_blueprint(users, url_prefix='/api/v1/users')

    from flask import render_template, send_from_directory

    @app.route('/<path:filename>')
    def file(filename):
        from os import path
        return send_from_directory(path.join(app.root_path, 'templates'), filename)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app