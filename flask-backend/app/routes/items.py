from flask import Blueprint

bp = Blueprint("items", __name__)

@bp.route("/")
def get_items():
    return "<h1>ITEM</h1>"
