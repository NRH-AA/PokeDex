# import statement for CSRF
from flask import Flask, request
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .routes import pokemon, items
from .config import Configuration
from flask_migrate import Migrate
from .models import db

import os

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)
Migrate(app, db)

app.register_blueprint(pokemon.bp, url_prefix="/api/pokemon")
app.register_blueprint(items.bp, url_prefix="/api/items")


@app.route('/')
def index():
    return "<p>Working</p>"


# after request code for CSRF token injection
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
