import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/recipe_info', methods=('GET', 'POST'))
def recipe_info():
    return json.dumps({
        "ingredient_name": {
            "units": "unit_name",
            "n_units": 4, 
            "per_unit": {
                "calories": 9001,
                "carbon": 50,
                "cost": 10.51,
            },
            "substitutions": {
                "etc":"etc"
            }
        }
    })

