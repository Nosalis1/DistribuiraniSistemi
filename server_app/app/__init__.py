from flask import Flask  # type:ignore
from .config import Config
from .extensions import db, ma, migrate
from .views import featurex_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(featurex_bp)

    return app
