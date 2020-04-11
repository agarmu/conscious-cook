## Send: 
```json
["ingredient1_name", "ingredient2_name", "..."]
```
## Recieve:
```json
{
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
}
```