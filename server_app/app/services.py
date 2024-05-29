from .models import FeatureX
from .extensions import db


def get_all_featurex():
    return FeatureX.query.all()


def get_featurex_by_id(featurex_id):
    return FeatureX.query.get(featurex_id)


def create_featurex(data):
    new_featurex = FeatureX(**data)
    db.session.add(new_featurex)
    db.session.commit()
    return new_featurex
