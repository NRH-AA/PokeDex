from flask import Blueprint, request
from ..models import db, Item
from .forms import ItemForm

bp = Blueprint("items", __name__)


@bp.route("/<int:id>", methods=["PUT"])
def edit_items(id):
    form = ItemForm()

    item = Item.query.get(id)

    if form.is_submitted():
        form["csrf_token"].data = request.cookies["csrf_token"]

        item.name = form.data["name"]
        item.happiness = form.data["happiness"]
        item.price = form.data["price"]

        db.session.commit()

        return item.to_dict()


@bp.route("/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get(id)

    db.session.delete(item)
    db.session.commit()

    return {"id": id}
