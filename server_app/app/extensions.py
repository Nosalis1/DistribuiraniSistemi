from flask_sqlalchemy import SQLAlchemy  # type:ignore
from flask_marshmallow import Marshmallow  # type:ignore
from flask_migrate import Migrate  # type:ignore

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
