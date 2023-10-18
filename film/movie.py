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


#P6: en actor
@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    pelicula = db.execute(
        """SELECT title AS titulo, rental_duration AS duracion_alquiler, release_year AS año, description AS descripcion
        FROM film
        WHERE film_id = ?
        ORDER BY title ASC""",
        (id,)
    ).fetchone()
    actores = db.execute(
        """SELECT a.actor_id, a.first_name, a.last_name
        FROM film_actor fa join actor a on a.actor_id = fa.actor_id
        WHERE fa.film_id = ?""", 
        (id,)
    ).fetchall()
    return render_template('movie/detalle.html', pelicula=pelicula, actores=actores)