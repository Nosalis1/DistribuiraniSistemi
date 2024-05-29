from flask import Blueprint, request, jsonify  # type:ignore
from .services import get_all_featurex, get_featurex_by_id, create_featurex
from .schemas import FeatureXSchema

featurex_bp = Blueprint("featurex", __name__)
featurex_schema = FeatureXSchema()
featuresx_schema = FeatureXSchema(many=True)


@featurex_bp.route("/api/featurex", methods=["GET"])
def get_featurex():
    featuresx = "Hello From Server"  # get_all_featurex()
    return jsonify(featuresx)  # featuresx_schema.jsonify(featuresx)


@featurex_bp.route("/api/featurex/<int:id>", methods=["GET"])
def get_featurex_detail(id):
    featurex = get_featurex_by_id(id)
    if featurex is None:
        return jsonify({"message": "FeatureX not found"}), 404
    return featurex_schema.jsonify(featurex)


@featurex_bp.route("/api/featurex", methods=["POST"])
def create_featurex():
    data = request.get_json()
    featurex = create_featurex(data)
    return featurex_schema.jsonify(featurex), 201
