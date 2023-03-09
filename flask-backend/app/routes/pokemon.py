from flask import Blueprint, request
from ..models import db, Pokemon, Item
from .forms import PokemonForm, ItemForm

bp = Blueprint("pokemon", __name__)


@bp.route("/", methods=["GET"])
def get_pokemon():
    pokemons = Pokemon.query.all()
    return [pokemon.to_dict() for pokemon in pokemons]


@bp.route("/<int:id>", methods=["GET"])
def get_one_pokemon(id):
    pokemon = Pokemon.query.get(id)
    return pokemon.to_dict()


@bp.route("/types", methods=["GET"])
def get_types():
    types = [
        "fire",
        "electric",
        "normal",
        "ghost",
        "psychic",
        "water",
        "bug",
        "dragon",
        "grass",
        "fighting",
        "ice",
        "flying",
        "poison",
        "ground",
        "rock",
        "steel",
    ]
    return types


@bp.route("/", methods=["POST"])
def create_pokemon():
    form = PokemonForm()

    if form.is_submitted():
        form["csrf_token"].data = request.cookies["csrf_token"]

        pokemon = Pokemon(
            number = form.data["number"],
            name = form.data["name"],
            attack = form.data["attack"],
            defense = form.data["defense"],
            imageUrl = form.data["imageUrl"],
            type = form.data["type"],
            moves = form.data["moves"],
            encounterRate = form.data["encounterRate"],
            catchRate = form.data["catchRate"],
            captured = form.data["captured"],
        )

        db.session.add(pokemon)
        db.session.commit()

        return pokemon.to_dict()


@bp.route("/<int:id>", methods=["PUT"])
def edit_pokemon(id):
    form = PokemonForm()

    pokemon = Pokemon.query.get(id)

    # if not pokemon:
    #     return {"errors": "Could not find pokemon."}

    if form.is_submitted():
        form["csrf_token"].data = request.cookies["csrf_token"]

        pokemon.number = form.data["number"]
        pokemon.name = form.data["name"]
        pokemon.attack = form.data["attack"]
        pokemon.defense = form.data["defense"]
        pokemon.imageUrl = form.data["imageUrl"]
        pokemon.type = form.data["type"]
        pokemon.moves = form.data["moves"]
        pokemon.encounterRate = form.data["encounterRate"]
        pokemon.catchRate = form.data["catchRate"]
        pokemon.captured = form.data["captured"]

        db.session.commit()

        return pokemon.to_dict()


@bp.route("/<int:id>", methods=["DELETE"])
def delete_pokemon(id):
    pokemon = Pokemon.query.get(id)

    db.session.delete(pokemon)
    db.session.commit()

    return {"message": "success"}


@bp.route("/<int:id>/items", methods=["GET"])
def get_items(id):
    pokemon = Pokemon.query.get(id)

    return [item.to_dict() for item in pokemon.items]


@bp.route("/<int:id>/items", methods=["POST"])
def post_items(id):
    form = ItemForm()

    if form.is_submitted():
        form["csrf_token"].data = request.cookies["csrf_token"]

        item = Item(
            name = form.data["name"],
            happiness = form.data["happiness"],
            imageUrl = "a.png",
            price = form.data["price"],
            pokemonId = id
        )

        db.session.add(item)
        db.session.commit()

        return item.to_dict()
