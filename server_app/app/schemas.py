from .extensions import ma
from .models import FeatureX


class FeatureXSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FeatureX
