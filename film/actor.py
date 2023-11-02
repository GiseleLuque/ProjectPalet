from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from film.db import get_db

bp = Blueprint('actor', __name__, url_prefix="/actor/")#nombra a todos actor al usar el prefix

#5:
#RUTA DE actores
@bp.route('/')
def index():
    db = get_db()
    actors = db.execute(
        "SELECT actor_id, first_name, last_name FROM actor ORDER BY first_name ASC;"
    ).fetchall()
    return render_template('actor/index.html', actors=actors)

#6: detalle de actor 
@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    actor = db.execute(
     """SELECT actor_id, first_name, last_name FROM actor 

        WHERE actor_id = ?    
        """,
        (id,)
    ).fetchone()

    peliculas = db.execute(
        """SELECT fa.actor_id, f.film_id, f.title, f.rental_duration, f.description
        FROM film f join film_actor fa on f.film_id = fa.film_id
        WHERE fa.actor_id = ?
        ;""",
        (id,)
    ).fetchall()
    return render_template('actor/detalle.html', actor=actor,  peliculas=peliculas)