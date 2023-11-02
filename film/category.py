from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from film.db import get_db

bp = Blueprint('category', __name__, url_prefix="/category/")#nombra a todos categorias al usar el prefix

#5:
#RUTA DE categorias
@bp.route('/')
def index():
    db = get_db()
    categories = db.execute(
        "SELECT name FROM category ORDER BY name ASC;"
    ).fetchall()
    return render_template('category/index.html', categories=categories)