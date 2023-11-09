from flask import (Blueprint, flash, g, redirect, render_template, request, url_for, jsonify)
from werkzeug.exceptions import abort

from film.db import get_db

bp = Blueprint('actor', __name__, url_prefix="/actor/")#nombra a todos actor al usar el prefix
bpapi = Blueprint('actor_api', __name__, url_prefix="/api/actor/")

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


##7) api de actor:
@bpapi.route('/')
def index_api():
    db = get_db()
    actors = db.execute(
        "SELECT actor_id, first_name, last_name FROM actor ORDER BY first_name ASC;"
    ).fetchall()

    for actor in actors:
        actor["detalle_url"] = url_for("actor_api.detalle_api", id=actor["actor_id"], _external=True)
    return jsonify(actors=actors)

#detalle api de actor:
@bpapi.route('/detalle/<int:id>')
def detalle_api(id):
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



    return jsonify(actor=actor,  peliculas=peliculas)

