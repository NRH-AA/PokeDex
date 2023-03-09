from app.models import db, Pokemon
from app import app
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    pokemon = Pokemon(
        number=1,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle, vine whip',
        captured=True,
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )

    pokemon2 = Pokemon(
        number=2,
        imageUrl='/images/pokemon_snaps/1.svg',
        name='Pikachu',
        attack=49,
        defense=49,
        type='grass',
        moves='tackle, vine whip',
        captured=False,
        createdAt=datetime.now(),
        updatedAt=datetime.now()
    )

    db.session.add(pokemon)
    db.session.add(pokemon2)
    db.session.commit()
