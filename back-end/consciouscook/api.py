import json
from pint import UnitRegistry
from fractions import Fraction
from flask import (
    Blueprint, render_template, request, url_for
)
from flask_cors import CORS

bp = Blueprint('api', __name__, url_prefix='/api')
CORS(bp)

def unpack_mixed_fraction(text):
    strings = text.split()
    total = 0
    i = 0
    for num in strings:
        try: 
            total += float(Fraction(num))
            i += 1
        except:
            break
    if total == 0:
        return text
    return str(total) + " " + " ".join(strings[i:])

ureg = UnitRegistry()
def get_quantity(text):
    words = unpack_mixed_fraction(text).split()
    while words:
        try:
            quantity = ureg.parse_expression(" ".join(words))
            return quantity
        except:
            words.pop()    
    return None

food_names = ["beef", "celery", "tofu", "orange soda", "eggs", "beef seasoning"]
food_names = list(sorted(food_names, key=len, reverse=True))
def get_food(text):
    for food in food_names:
        if food in text:
            return food

@bp.route('/recipe_info', methods=['POST'])
def recipe_info():
    info = {}
    request_json = request.get_json() 
    raw_ingredients = list(set(request_json.keys()))
    for ingredient in raw_ingredients:
        food_name = get_food(ingredient)
        quantity = get_quantity(ingredient)
        try:
            units = str(quantity.units)
        except:
            units = "unknown"
        try:
            n_units = str(quantity.magnitude)
        except: 
            n_units = "unknown"
        info[food_name] = {
            "units": units,
            "n_units": n_units,
            "per_unit": {
                "calories": 4000,
                "carbon": 5000,
                "cost": "600.00",
            },
            "element_id": request_json[ingredient],
            "substitutions": {
               "substitute1_name":{
                    "per_unit": {
                        "calories": 9002,
                        "carbon": 40,
                        "cost": "8.51",
                    }
                } 
            }
        }
    return json.dumps(info)

@bp.route('/recipe_info/example', methods=['GET', 'POST'])
def example_recipe_info():
    return json.dumps({
        "ingredient1_name": {
            "units": "unit_name",
            "per_unit": {
                "calories": 9001,
                "carbon": 50,
                "cost": 10.51,
            },
            "element_id": "ingredient1_id",
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
            "element_id": "ingredient2_id",
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

