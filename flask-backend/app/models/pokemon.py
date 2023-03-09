from .db import db

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageUrl = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.String(255), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounterRate = db.Column(db.Float, nullable=False, default=1.00)
    catchRate = db.Column(db.Float, nullable=False, default=1.00)
    captured = db.Column(db.Boolean, nullable=False, default=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)

    items = db.relationship("Item", back_populates="pokemon")


    def to_dict(self):
        return {
            "id": self.id,
            "number": self.number,
            "attack": self.attack,
            "defense": self.defense,
            "imageUrl": self.imageUrl,
            "name": self.name,
            "type": self.type,
            "moves": self.moves,
            "encounterRate": self.encounterRate,
            "catchRate": self.catchRate,
            "captured": self.captured,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "items": self.items
        }
