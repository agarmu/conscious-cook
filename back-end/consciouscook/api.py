import json
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/recipe_info', methods=('POST'))
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

@bp.route('/recipe_info/example', methods=('GET', 'POST'))
def example_recipe_info():
    return json.dumps({
        "ingredient1_name": {
            "units": "unit_name",
            "per_unit": {
                "calories": 9001,
                "carbon": 50,
                "cost": 10.51,
            },
            "substitutions": {
                "substitute1_name":{
                    "per_unit": {
                        "calories": 9002,
                        "carbon": 40,
                        "cost": 8.51,
                    }
                },
                "substitute2_name":{
                    "per_unit": {
                        "calories": 9003,
                        "carbon": 35,
                        "cost": 12.51,
                    }
                },
            }
        },
        "ingredient2_name": {
            "units": "unit_name",
            "per_unit": {
                "calories": 9001,
                "carbon": 50,
                "cost": 10.51,
            },
            "substitutions": {
                "substitute1_name":{
                    "per_unit": {
                        "calories": 9002,
                        "carbon": 40,
                        "cost": 8.51,
                    }
                },
                "substitute2_name":{
                    "per_unit": {
                        "calories": 9003,
                        "carbon": 35,
                        "cost": 12.51,
                    }
                },
            }
        }
    })

