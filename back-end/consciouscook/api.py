import json
import pint
from fractions import Fraction
from flask import (
    Blueprint, render_template, request, url_for
)
from flask_cors import CORS
import pandas as pd

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

ureg = pint.UnitRegistry()
def get_quantity(text):
    words = unpack_mixed_fraction(text).split()
    while words:
        try:
            quantity = ureg.parse_expression(" ".join(words))
            return quantity
        except:
            words.pop()
    return None

with open("consciouscook/data.json") as data:
    food_data = pd.read_json(data, orient="records")
    food_data["Food"] = food_data["Food"].str.lower()
    food_data = food_data.set_index("Food")
    print(food_data.loc["okra"])

food_names = list(sorted(food_data.index, key=len, reverse=True))
def get_food(text):
    for food in food_names:
        if food in text:
            return food.lower()   

@bp.route('/recipe_info', methods=['POST'])
def recipe_info():
    info = {}
    request_json = request.get_json() 
    raw_ingredients = list(set(request_json.keys()))
    for ingredient in raw_ingredients:
        food_name = get_food(ingredient)
        try:
            food_row = food_data.loc[food_name]
        except KeyError:
            continue

        if not food_name:
            print("could not find food name")
            continue

        quantity = get_quantity(ingredient)
        if quantity:
            try:
                food_mass = quantity.to('gram').magnitude
                grams_per_orig_unit = food_mass/quantity.magnitude
            except pint.errors.DimensionalityError:
                 # try volumetric
                try: 
                    conversion_factor = food_row["Density (grams-per-cup)"]
                    food_mass = quantity.to('cup') * conversion_factor * ureg.gram/ureg.cup
                    food_mass = food_mass.to_reduced_units().magnitude
                    grams_per_orig_unit = food_mass/quantity.magnitude 
                except pint.errors.DimensionalityError:
                    quantity = None
                    food_mass = None
        else:
            continue
        try:
            units = str(quantity.units)
        except:
            units = "unknown"
        try:
            n_units = str(quantity.magnitude)
        except: 
            n_units = "unknown"
        per_unit_stats = {
            "calories": str(round(food_row["Calories-per-gram"] * grams_per_orig_unit)),
            "carbon": str(round(food_row["CO2-percent"] * grams_per_orig_unit)),
            "cost": str(round(food_row["Price-per-gram"] * grams_per_orig_unit)),
        }
        info[food_name] = {
            "units": units,
            "n_units": n_units,
            "per_unit": per_unit_stats,
            "element_id": request_json[ingredient],
            "carbon_rating": str(food_row["CO2-percent"]/food_row["Calories-per-gram"]),
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

