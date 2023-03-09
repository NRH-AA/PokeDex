from .db import db
from .pokemon import Pokemon

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemonId = db.Column(db.Integer, db.ForeignKey(Pokemon.id))

    pokemon = db.relationship("Pokemon")

    def to_dict(self):
        return {
            "id": self.id,
            "happiness": self.happiness,
            "imageUrl": self.imageUrl,
            "name": self.name,
            "price": self.price,
            "pokemonId": self.pokemonId
        }
