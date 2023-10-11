from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from film.db import get_db

bp = Blueprint('movie', __name__)

@bp.route('/')
def index():
    db = get_db()
    movies = db.execute(
        "SELECT film_id, title, release_year, description FROM film ORDER BY title ASC;"
    ).fetchall()
    return render_template('movie/index.html', movies=movies)


@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT title AS titulo, rental_duration AS duracion_alquiler, release_year AS año, description AS descripcion
        FROM film
        WHERE film_id = ?
        ORDER BY title ASC;""",
        (id,)
    ).fetchone()
    return render_template('movie/detalle.html', pelicula=pelicula)