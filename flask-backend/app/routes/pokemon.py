from flask import Blueprint

bp = Blueprint("pokemon", __name__)

@bp.route("/")
def get_pokemon():
    return "<h1>POKEMON</h1>"
