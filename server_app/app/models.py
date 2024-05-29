from .extensions import db


class FeatureX(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<FeatureX {self.title}>"
